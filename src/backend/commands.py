#! /usr/bin/env python

import sys
import paramiko
import psycopg2
        
def main():
    # Hostname plus command-line arguments
    pg_hostname = 'cse182-db.lt.ucsc.edu'
    pg_username = sys.argv[1]
    ucsc_password = sys.argv[2]
    pg_password = sys.argv[3]

    # Steps needed to connect to UCSC Unix Server
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.get_host_keys().add('unix.ucsc.edu', 'ssh-rsa', 'hostkey')
    ssh_client.set_missing_host_key_policy(paramiko.WarningPolicy())
    ssh_client.connect('unix.ucsc.edu', username=pg_username, password=ucsc_password)

    # Steps needed to connect to PostgreSQL server in Unix server
    conn = psycopg2.connect(host=pg_hostname, user=pg_username, password=pg_password)
    cursor = conn.cursor()

    # Step 1: Alter the ROLE
    cursor.execute("ALTER ROLE parunsha SET search_path TO FileRetriever;")
    conn.commit()

    # Step 2: Load the schema file data into PostgreSQL
    schema_file_path = "/Users/prithvi/Library/CloudStorage/OneDrive-Personal/desktop_clutter/FileRetriever_Test/src/database/create_fileretriever.sql"
    with open(schema_file_path, "r") as schema_file:
        schema_sql = schema_file.read()
        cursor.execute(schema_sql)
        conn.commit()

    # Step 3: Load the data file into PostgreSQL
    data_file_path = "/Users/prithvi/Library/CloudStorage/OneDrive-Personal/desktop_clutter/FileRetriever_Test/src/database/load_testretriever.sql"
    data_file = open(data_file_path, "r")
    data_style = data_file.readline()
    data_style = data_style.strip(";\n")
    data_style_parts = data_style.split(" ")
    schema_name, delimiter = data_style_parts[1], data_style_parts[len(data_style_parts) - 1]
    cursor.copy_from(data_file, schema_name.lower(), sep=delimiter[1], null='')
    conn.commit()

    # Step 4: Print out the loaded data
    print_table = "SELECT * FROM " + schema_name + ";"
    cursor.execute(print_table)
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    print(columns)
    print(data)
    conn.commit()

    # Step 5: Close everything
    schema_file.close()
    data_file.close()
    cursor.close()
    conn.close()
    ssh_client.close()

if __name__ == '__main__':
    main()


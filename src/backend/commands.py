#! /usr/bin/env python

import sys
import psycopg2
from psycopg2 import Error

def main():
    # Hostname plus command-line arguments
    pg_hostname = sys.argv[1]
    pg_username = sys.argv[2]
    pg_dbname = sys.argv[3]

    # Steps needed to connect to PostgreSQL server
    try:
        conn = psycopg2.connect(host=pg_hostname, user=pg_username, password="", dbname=pg_dbname)
        cursor = conn.cursor()
    except Error as e:
        print(e)

    # Step 1: Alter the ROLE
    try:
        cursor.execute("ALTER ROLE prithvi SET search_path TO fileretrieve;")
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print(e)

    # Step 2: Load the schema file data into PostgreSQL
    try:
        schema_file_path = "../database/create_fileretriever.sql"

        with open(schema_file_path, "r") as schema_file:
            schema_sql = schema_file.read()
            cursor.execute(schema_sql)
            conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print(e)

    # Step 3: Load the data file into PostgreSQL
    try:
        data_file_path = "../database/load_testretriever.sql"

        data_file = open(data_file_path, "r")
        data_style = data_file.readline()
        data_style = data_style.strip(";\n")
        data_style_parts = data_style.split(" ")
        schema_name, delimiter = data_style_parts[1], data_style_parts[len(data_style_parts) - 1]
        cursor.copy_from(data_file, schema_name.lower(), sep=delimiter[1], null='')
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print(e)

    # Step 4: Load query file
    try:
        query_file_path = '../database/queries_testretriever.sql'
        
        with open(query_file_path, 'r') as query_file:
            for line in query_file:
                filename = line[59:line.rfind(':') - 1]
                new_filename = filename.replace("'", "''")
                new_filename = new_filename.replace(":", "/")
                line = line.replace(filename, new_filename)
                colon_index = line.rfind(':')
                line = line[0:colon_index] + ', ' + line[colon_index+1:]
                cursor.execute(line)

        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print(e)

    # Step 5: Print out the loaded data
    try:
        print_table = "SELECT * FROM " + schema_name + " f ORDER BY f.filesize DESC, f.filename;"
        cursor.execute(print_table)
        data = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        print(columns)
        print(data)
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        print(e)

    # Step 6: Close everything
    schema_file.close()
    query_file.close()
    data_file.close()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()

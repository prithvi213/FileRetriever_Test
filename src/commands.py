#! /usr/bin/env python

import sys
import paramiko
import psycopg2

def set_search_path(conn, username, pathname):
    try:
        cursor = conn.cursor()

        if(username is None or pathname is None):
            cursor.close()
            conn.close()
            return -1

        stmt = "ALTER ROLE %s SET SEARCH_PATH TO %s"
        cursor.execute(stmt, (username, pathname))
        cursor.close()
        return 0
    except:
        cursor.close()
        conn.close()
        sys.exit(-1)

def main():
    pg_hostname = 'cse182-db.lt.ucsc.edu'
    pg_username = sys.argv[1]
    ucsc_password = sys.argv[2]
    pg_password = sys.argv[3]


    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.get_host_keys().add('unix.ucsc.edu', 'ssh-rsa', 'hostkey')
    ssh_client.set_missing_host_key_policy(paramiko.WarningPolicy())
    ssh_client.connect('unix.ucsc.edu', username=pg_username, password=ucsc_password)

    conn = psycopg2.connect(host=pg_hostname, user=pg_username, password=pg_password)

    set_search_path(conn, username='parunsha', pathname='FileRetriever')

    conn.close()
    ssh_client.close()

if __name__ == '__main__':
    main()


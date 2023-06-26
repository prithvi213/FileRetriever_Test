#! /usr/bin/env python

import sys
import paramiko
import psycopg2

def main():
    pg_hostname = 'cse182-db.lt.ucsc.edu'
    pg_username = sys.argv[1]
    ucsc_password = sys.argv[2]
    pg_password = sys.argv[3]
    print(pg_username)
    print(ucsc_password)
    print(pg_password)


    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.get_host_keys().add('unix.ucsc.edu', 'ssh-rsa', 'hostkey')
    ssh_client.set_missing_host_key_policy(paramiko.WarningPolicy())
    ssh_client.connect('unix.ucsc.edu', username=pg_username, password=ucsc_password)

    myConn = psycopg2.connect(host=pg_hostname, user=pg_username, password=pg_password)
    cursor = myConn.cursor()

    print("SUCCESSFUL CONNECTION")


    myConn.close()
    ssh_client.close()

if __name__ == '__main__':
    main()


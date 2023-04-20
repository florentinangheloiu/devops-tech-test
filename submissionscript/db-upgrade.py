#!/usr/bin/env python3

import os
import re
import mysql.connector
import sys

def get_scripts(dir):
    sql_scripts = []
    for filename in os.listdir(dir):
        if re.match(r'^\d+.*\.sql$', filename):
            sql_scripts.append(filename)
    sql_scripts.sort()
    return sql_scripts

def get_current_version(conn):
    mycursor = conn.cursor()
    mycursor.execute("SELECT MAX(version) FROM versionTable")
    myresult = [i[0] for i in mycursor.fetchall()]
    return int(myresult[0])

def update_version(conn, version):
    mycursor = conn.cursor()
    mycursor.execute(f"UPDATE versionTable SET version = {version}")
    conn.commit()

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("The following parameters are needed to run the script: directory-with-sql-scripts username-for-the-db db-host db-name db-password")
        sys.exit(1),

    directory = sys.argv[1]
    username = sys.argv[2]
    host = sys.argv[3]
    dbname = sys.argv[4]
    password = sys.argv[5]

    conn = mysql.connector.connect(
        host=host,
        database=dbname,
        user=username,
        password=password
    )

    all_scripts = get_scripts(directory)
    print(f"Found filenames that match the necessary pattern: {all_scripts}")

    current_version = get_current_version(conn)
    print(f"Current database version is {current_version}")
import os
import re

def get_scripts(dir):
    sql_scripts = []
    for filename in os.listdir(dir):
        if re.match(r'^\d+', filename):
            sql_scripts.append(filename)
    sql_scripts.sort()
    return sql_scripts

all_files = get_scripts("dbscripts")
print(f"Found filenames that match the necessary pattern: {all_files}")
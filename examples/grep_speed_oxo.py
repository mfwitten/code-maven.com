import sys
import re

if len(sys.argv) != 3:
    exit(f"{sys.argv[0]} FILENAME LIMIT")

_, filename, limit = sys.argv

def grep(regex, fh):
    for line in fh:
        if regex.search(line):
            print(line, end='')

i = int(limit)

y = re.compile(r'(.)y\1')
with open(filename) as fh:
    while i:
        i-=1
        grep(y, fh)
        fh.seek(0)

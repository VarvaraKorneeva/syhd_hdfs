#!/usr/bin/python
import sys


for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    try:
        temp = float(words[8])
        month = words[1][6:8]
    except:
        continue
    print('%s\t%s' % (month, temp))

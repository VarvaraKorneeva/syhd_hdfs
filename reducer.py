#!/usr/bin/python
import sys


current_month = None
current_sum_temp = 0
current_count = 0
month = None
for line in sys.stdin:
    line = line.strip()
    month, temp = line.split('\t', 1)
    if current_month == month:
        current_sum_temp += temp
        current_count += 1
    else:
        if current_month:
            print('%s\t%s' % (current_month, current_sum_temp / current_count))
        current_month = month
        current_count = 0
        current_sum_temp = temp
if current_month == month:
    print('%s\t%s' % (current_month, current_sum_temp / current_count))

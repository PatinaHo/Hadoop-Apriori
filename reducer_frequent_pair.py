#!/usr/bin/env python
# mapper_frequent_pair

from operator import itemgetter
import sys

frequent_itemset = {}
with open("./frequent_itemset.txt") as infile:
    for line in infile:
        line = line.strip().split('\t')
        frequent_itemset[line[0]] = line[1]

minsupport = 100
current_pair = None
current_count = 0
pair = None

for line in sys.stdin:
    line = line.strip()
    pair, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:  #ignore if count is not an integer
        continue
    if current_pair == pair:
        current_count += count
    else:
        if current_pair:
            if(current_count > minsupport):
                print(current_pair +'\t'+str(current_count))
        current_count = count
        current_pair = pair

if pair == current_pair:
    if(current_count > minsupport):
        print(current_pair+'\t'+str(current_count))
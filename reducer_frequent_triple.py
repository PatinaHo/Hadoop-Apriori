#!/usr/bin/env python
# mapper_frequent_pair

from operator import itemgetter
import sys

frequent_pairset = {}
with open("./frequent_pairset.txt") as infile:
    for line in infile:
        line = line.strip().split('\t')
        frequent_pairset[line[0]] = line[1]

minsupport = 50
current_triple = None
current_count = 0
triple = None

for line in sys.stdin:
    line = line.strip()
    triple, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:  #ignore if count is not an integer
        continue
    if current_triple == triple:
        current_count += count
    else:
        if current_triple:
            if(current_count > minsupport):
                print(current_triple+'\t'+str(current_count))
        current_count = count
        current_triple = triple

if triple == current_triple:
    if(current_count > minsupport):
        print(current_triple+'\t'+str(current_count))
#!/usr/bin/env python
# mapper_frequent_triple

import sys

frequent_itemset = {}
with open("./frequent_itemset.txt") as infile:
    for line in infile:
        line = line.strip().split('\t')
        frequent_itemset[line[0]] = line[1]

for line in sys.stdin:
	line = line.strip().split('\t')
	keyA = line[0].split(' ')[0]
	keyB = line[0].split(' ')[1]
	pair_count = line[1]
	prob = int(pair_count) / (1.0*int(frequent_itemset[keyA]))
	print(keyA+'->'+keyB+':'+str(prob))
	prob = int(pair_count) / (1.0*int(frequent_itemset[keyB]))
	print(keyB+'->'+keyA+':'+str(prob))
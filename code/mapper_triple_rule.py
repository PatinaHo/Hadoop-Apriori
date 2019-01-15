#!/usr/bin/env python
# mapper_triple_rule.py

import sys

frequent_pairset = {}
with open("./frequent_pairset.txt") as infile:
    for line in infile:
        line = line.strip().split('\t')
        frequent_pairset[line[0]] = line[1]

for line in sys.stdin:
	line = line.strip().split('\t')
	keyA = line[0].split(' ')[0]
	keyB = line[0].split(' ')[1]
	keyC = line[0].split(' ')[2]
	triple_count = line[1]

	pair1 = keyA+' '+keyB
	prob = int(triple_count) / (1.0 * int(frequent_pairset[pair1]))
	print(pair1+'->'+keyC+':'+str(prob))
	pair2 = keyA+' '+keyC
	prob = int(triple_count) / (1.0 * int(frequent_pairset[pair2]))
	print(pair2+'->'+keyB+':'+str(prob))
	pair3 = keyB+' '+keyC
	prob = int(triple_count) / (1.0 * int(frequent_pairset[pair3]))
	print(pair3+'->'+keyA+':'+str(prob))

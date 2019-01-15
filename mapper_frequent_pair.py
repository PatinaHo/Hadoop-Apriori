#!/usr/bin/env python
# mapper_frequent_pair

import sys

frequent_itemset = {}
with open("./frequent_itemset.txt") as infile:
    for line in infile:
        line = line.strip().split('\t')
        frequent_itemset[line[0]] = line[1]

pair_counts = {}
for basket in sys.stdin:
    basket = basket.strip().split(" ")
    for i in range(len(basket)):
        for j in range(i+1, len(basket)):
            if(basket[i] in frequent_itemset) and (basket[j] in frequent_itemset):
                if(basket[i]<basket[j]):
                    pair = (basket[i], basket[j])
                else:
                    pair = (basket[j], basket[i])
                if(pair in pair_counts):
                    pair_counts[pair]+=1
                else:
                    pair_counts[pair]=1

for pair, counts in pair_counts.items():
    print(pair[0]+' '+pair[1], end='')
    print('\t'+str(counts))
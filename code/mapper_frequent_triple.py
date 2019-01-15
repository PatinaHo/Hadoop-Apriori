#!/usr/bin/env python
# mapper_frequent_triple

import sys

frequent_itemset = {}
with open("./frequent_itemset.txt") as infile:
    for line in infile:
        line = line.strip().split('\t')
        frequent_itemset[line[0]] = line[1]

frequent_pairset = {}
with open("./frequent_pairset.txt") as infile:
    for line in infile:
        line = line.strip().split('\t')
        pair = tuple(line[0].split(" "))
        frequent_pairset[pair] = line[1]

triple_counts = {}
for basket in sys.stdin:
    basket = basket.strip().split(" ")
    for i in range(len(basket)):
        for j in range(i+1, len(basket)):
            for k in range(j + 1, len(basket)):
                if(basket[i] in frequent_itemset) and (basket[j] in frequent_itemset) and (basket[k] in frequent_itemset):
                    # situation 1
                    if basket[i] <= basket[j] <= basket[k]:
                        pair1 = (basket[i], basket[j])
                        pair2 = (basket[i], basket[k])
                        pair3 = (basket[j], basket[k])
                        if (pair1 in frequent_pairset) and (pair2 in frequent_pairset) and (pair3 in frequent_pairset):
                            triple = (basket[i], basket[j], basket[k])
                            if triple in triple_counts:
                                triple_counts[triple] = triple_counts[triple] + 1
                            else:
                                triple_counts[triple] = 1
                    # situation 2
                    elif basket[i] <= basket[k] <= basket[j]:
                        pair1 = (basket[i], basket[k])
                        pair2 = (basket[i], basket[j])
                        pair3 = (basket[k], basket[j])
                        if (pair1 in frequent_pairset) and (pair2 in frequent_pairset) and (pair3 in frequent_pairset):
                            triple = (basket[i], basket[k], basket[j])
                            if triple in triple_counts:
                                triple_counts[triple] = triple_counts[triple] + 1
                            else:
                                triple_counts[triple] = 1
                    # situation 3
                    elif basket[k] <= basket[i] <= basket[j]:
                        pair1 = (basket[k], basket[i])
                        pair2 = (basket[k], basket[j])
                        pair3 = (basket[i], basket[j])
                        if (pair1 in frequent_pairset) and (pair2 in frequent_pairset) and (pair3 in frequent_pairset):
                            triple = (basket[k], basket[i], basket[j])
                            if triple in triple_counts:
                                triple_counts[triple] = triple_counts[triple] + 1
                            else:
                                triple_counts[triple] = 1
                    # situation 4
                    elif basket[k] <= basket[j] <= basket[i]:
                        pair1 = (basket[k], basket[j])
                        pair2 = (basket[k], basket[i])
                        pair3 = (basket[j], basket[i])
                        if (pair1 in frequent_pairset) and (pair2 in frequent_pairset) and (pair3 in frequent_pairset):
                            triple = (basket[k], basket[j], basket[i])
                            if triple in triple_counts:
                                triple_counts[triple] = triple_counts[triple] + 1
                            else:
                                triple_counts[triple] = 1
                    # situation 5
                    elif basket[j] <= basket[i] <= basket[k]:
                        pair1 = (basket[j], basket[i])
                        pair2 = (basket[j], basket[k])
                        pair3 = (basket[i], basket[k])
                        if (pair1 in frequent_pairset) and (pair2 in frequent_pairset) and (pair3 in frequent_pairset):
                            triple = (basket[j], basket[i], basket[k])
                            if triple in triple_counts:
                                triple_counts[triple] = triple_counts[triple] + 1
                            else:
                                triple_counts[triple] = 1
                    # situation 6
                    elif basket[j] <= basket[k] <= basket[i]:
                        pair1 = (basket[j], basket[k])
                        pair2 = (basket[j], basket[i])
                        pair3 = (basket[k], basket[i])
                        if (pair1 in frequent_pairset) and (pair2 in frequent_pairset) and (pair3 in frequent_pairset):
                            triple = (basket[j], basket[k], basket[i])
                            if triple in triple_counts:
                                triple_counts[triple] = triple_counts[triple] + 1
                            else:
                                triple_counts[triple] = 1

for triple, counts in triple_counts.items():
    print(triple[0]+' '+triple[1]+' '+triple[2], end='')
    print('\t'+str(counts))
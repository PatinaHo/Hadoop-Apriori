#!/usr/bin/env python
# mapper_frequent_item

import sys
item_counts = {}
for basket in sys.stdin:
    basket = basket.strip()
    items = basket.split()
    for item in items:
        if(item in item_counts):
            item_counts[item]+=1
        else:
            item_counts[item]=1

for item, counts in item_counts.items():
    print(item+'\t'+ str(counts))
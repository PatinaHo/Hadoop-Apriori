#!/usr/bin/env python
from operator import itemgetter
import sys

minsupport = 100
current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:  #ignore if count is not an integer
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            if(current_count > minsupport):
                print(current_word+'\t'+str(current_count))
        current_count = count
        current_word = word

if word == current_word:
    if(current_count > minsupport):
        print(current_word+'\t'+str(current_count))
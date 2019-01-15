import operator
import sys

if (len(sys.argv)==2):
	f = open(sys.argv[1])
	data = f.readlines()
	f.close()

	rules = {}
	for line in data:
		line = line.strip().split(":")
		rules[line[0]] = float(line[1])

	sorted_rules = sorted(rules.items(), key=operator.itemgetter(1), reverse=True)
	f = open(sys.argv[1], 'w')
	for item in sorted_rules:
	    f.write(item[0]+' : '+str(item[1])+'\n')
	f.close()

else:
	print("Wrong argument.")
echo "Part1 start..."
hadoop fs -rm -R ./patina/final_output/pass1
yarn jar $HADOOP_STREAMING -files mapper_frequent_item.py,reducer_frequent_item.py -mapper 'python3 mapper_frequent_item.py' -reducer 'reducer_frequent_item.py' -input ./patina/browsing.txt -output ./patina/final_output/pass1
hadoop fs -cat ./patina/final_output/pass1/* > frequent_itemset.txt
hadoop fs -rm ./patina/frequent_itemset.txt
hadoop fs -copyFromLocal frequent_itemset.txt ./patina

echo "Part2 start..."
hadoop fs -rm -R ./patina/final_output/pass2
yarn jar $HADOOP_STREAMING -files mapper_frequent_pair.py,reducer_frequent_pair.py,frequent_itemset.txt -mapper 'python3 mapper_frequent_pair.py' -reducer 'reducer_frequent_pair.py' -input ./patina/browsing.txt -output ./patina/final_output/pass2
hadoop fs -cat ./patina/final_output/pass2/* > frequent_pairset.txt
hadoop fs -rm ./patina/frequent_pairset.txt
hadoop fs -copyFromLocal frequent_pairset.txt ./patina

echo "Part3 start..."
hadoop fs -rm -R ./patina/final_output/pass3
yarn jar $HADOOP_STREAMING -files mapper_frequent_triple.py,reducer_frequent_triple.py,frequent_itemset.txt,frequent_pairset.txt -mapper 'python3 mapper_frequent_triple.py' -reducer 'reducer_frequent_triple.py' -input ./patina/browsing.txt -output ./patina/final_output/pass3
hadoop fs -cat ./patina/final_output/pass3/* > frequent_tripleset.txt
hadoop fs -rm ./patina/frequent_tripleset.txt
hadoop fs -copyFromLocal frequent_tripleset.txt ./patina

echo "Generate pairrule..."
hadoop fs -rm -R ./patina/final_output/pairrule
yarn jar $HADOOP_STREAMING -files mapper_pair_rule.py,frequent_itemset.txt -mapper 'python3 mapper_pair_rule.py' -input ./patina/frequent_pairset.txt -output ./patina/final_output/pairrule
hadoop fs -cat ./patina/final_output/pairrule/* > pairrule.txt
python rule_sort.py pairrule.txt

echo "Generate triplerule..."
hadoop fs -rm -R ./patina/final_output/triplerule
yarn jar $HADOOP_STREAMING -files mapper_triple_rule.py,frequent_pairset.txt -mapper 'python3 mapper_triple_rule.py' -input ./patina/frequent_tripleset.txt -output ./patina/final_output/triplerule
hadoop fs -cat ./patina/final_output/triplerule/* > triplerule.txt
python rule_sort.py triplerule.txt

exit
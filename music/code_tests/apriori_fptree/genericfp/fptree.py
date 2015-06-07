from simplefp import *
from simplefpminer import SimpleFPMiner
import sys
#'''
# Main

if len(sys.argv) < 2:
	print "argv[1] required. Given argv:", sys.argv
	exit()

f = open(sys.argv[1], "r")
if not f:
	print "BAD FILE"
	exit()
lines = f.read().split("\n")


#create tuples
transactions = list()
for l in lines:
	ti = l.split(" ",1)
	tid = ti[0]
	items = ti[1].split(" ")
	for item in items:
		transactions.append( (tid,item) ) 
	
#Feed this to the fptree
fpt = SimpleFPTree()
fpt.set_transactions(transactions)
fpt.compute_L()
fpt.construct_tree()
fpt.print_tree()

print fpt.mine_frequencies()

#print fpm.conditional_base

'''
#
'''
#Due to cyclic dependencies, All imports are now at the bottom of the page


class SimpleFPMiner:
	
	def __init__(self, fptree):
		self.tree = fptree
		self.freq_patterns = list()
		self.temp_list = None
		self.conditional_base = dict()	# suffix_item => [list_of_conditional_bases]
		self.conditional_tree = dict()	# suffix_item => [list_of_conditional_bases]
		self.suffixes = list()
		
	
	def moveup(self, node,itemid):
		""" recursively moves up the tree to generate the conditional pattern base """
		if node.parent is None:
			return
		self.moveup(node.parent,itemid)
		self.temp_base.append( node.itemid  )
	
	def gen_conditional_base(self,itemid):
		"""Generates conditional base with the given itemid as suffix """
		self.conditional_base[itemid] = list()
		for node in self.tree.item_header.table[itemid]: #Use each itemid as suffix and try
			self.temp_base = list()
			self.moveup(node.parent,itemid)	# We do not need the suffix on the node
			if self.temp_base:	#If not empty
				self.conditional_base[itemid].append( (self.temp_base,node.count) )
		
	
	def gen_conditional_tree(self,suffixid):
		""" Takes a conditional base, Gives you the conditional tree """
		
		#Those without conditional bases will have empty conditional trees
		if not self.conditional_base[suffixid]:			
			return
			
		fpt = SimpleFPTree()
		#fpt = self.conditional_tree[suffixid]
		fpt.transactions = dict()
		i=0
		#Fill up transactions manually
		for (itemid_list,count) in self.conditional_base[suffixid]:
			fpt.transactions[i] = list()
			for itemid in itemid_list:
				fpt.transactions[i].append( (itemid,count) )	#Arbitrary transactionid
			i+=1
		fpt.compute_L()
		
		fpt.construct_tree()
		fpt.set_min_support(self.tree.min_support)
		fpt.prune_tree()
		
		if fpt.root.children:
			self.conditional_tree[suffixid] = fpt
		
	

	def gen_conditional_bases(self):
		""" Picks each item as a suffix and Generates conditional bases for each of them """
		for (itemid,count) in self.tree.L:	
			self.suffixes.append( (itemid,count) )
			self.gen_conditional_base(itemid)
	
	def gen_conditional_trees(self):
		""" Picks each suffix and generates conditional trees from their conditional bases"""
		for (itemid,count) in self.tree.L:
			self.gen_conditional_tree(itemid)
		
	
	def mine(self):	#Simpler version
		""" Generates frequency patterns for self.tree from the suffixes and the """
		self.gen_conditional_bases()
		self.gen_conditional_trees()
		#Do not allow those with no conditional bases to proceed
		
		
		for suffix in self.conditional_tree:
			subtree = self.conditional_tree[suffix]
			'''
			if not subtree.root.children:	#Should never reach here since generating an empty conditional tree is avoided
				print "FPMiner::mine, suffix loop. THIS SHOULD NOT HAVE HAPPENED"
				continue
			'''
			result = subtree.mine_frequencies() #fpm.mine()
			
			for fpattern in result:
				(patt,c) = fpattern
				patt.append(suffix)
				self.freq_patterns.append( (patt,c) )
			
		#Base case: Length 1 patterns
		for (suffix,count) in self.suffixes:
			if count >= self.tree.min_support:
				self.freq_patterns.append( ([suffix],count ))
		return self.freq_patterns
		
	
# Imports #	
from simplefp import *
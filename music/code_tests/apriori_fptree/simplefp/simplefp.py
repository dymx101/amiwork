#Due to cyclic dependencies, All imports are now at the bottom of the page

class SimpleFPTreeNode:
	def __init__(self, itemid,tree,parent):
		self.tree = tree
		self.itemid = itemid
		self.count = 0
		self.children = dict()	#need fast lookups
		self.tree.item_header.add_entry(self.itemid, self)	#Append this to the item header table
		self.parent = parent
		self.is_pruned = False
		
	def add_child(self, itemid,count=1):
		if self.children.get(itemid) is None:
			self.children[itemid] = SimpleFPTreeNode(itemid, self.tree, self)
		self.children[itemid].count += count
		
	
	def delete_child(self,itemid):
		del(self.children[itemid])
	
	
	
class SimpleFPHeader:
	def __init__(self, tree):
		self.tree = tree
		self.table = dict()
		
	def add_entry(self,itemid,pointer):
		if self.table.get(itemid) is None:
			self.table[itemid] = list()
		self.table[itemid].append(pointer)
		
		
class SimpleFPTree:
	""" Takes keys, Makes fptree """
	#Ok, I have no clue how to write python -_-
	def __init__(self):
		 self.transactions = dict()	#Takes the form tid => (itemid, count) ( count always 1 for the initial tree )
		 self.L = list()
		 self.headerList = dict()
		 self.root = None
		 self.item_header = SimpleFPHeader(self)
		 self.min_support = 0 
	
	def dump_transactions(self):
		for tid in self.transactions:
			str = tid + ": [ "
			for item in self.transactions[tid]:
				str+= item + ", "
			str+= "]"
			print str

	def set_min_support(self,min_support):
		self.min_support = min_support
	
	
	def set_transactions(self, transactions):
		""" Takes list of (transactionId, item ) and stores them in the member var"""
		for (tid, itemid) in transactions:
			tid = int(tid) 
			itemid = int(itemid)
			if self.transactions.get(tid) is None:
				self.transactions[tid] = list()
			self.transactions[tid].append( (itemid,1) )	#1 is the default count
	
	
	def compute_L(self):
		"""Computes L: The list of (transaction, list_of_items) where list_of_items is sorted in decreasing order of frequency"""
		self.count = dict()
		for tid in self.transactions:
			for (item,count) in self.transactions[tid]:
				if self.count.get(item) is None:
					self.count[item] = 0
				self.count[item]+= count
		
		count_desc =  sorted(self.count,key=self.count.get, reverse=True)
		
		for k in count_desc:#self.count: #Sort by count
			self.L.append( (k, self.count[k]) )
		
		if not self.count:
			min_support = 0
		else:
			min_support = self.count[count_desc[-1]]
		self.set_min_support(min_support)
		for tid in self.transactions:
			self.transactions[tid]= sorted( self.transactions[tid], cmp=self.freq_comparator, reverse=True)
			
		
	
	def construct_tree(self):
		""" Constructs the FP Tree from given transactions"""
		self.root = SimpleFPTreeNode("root", self, None)
		#self.item_header.add_entry("root",self)
		
		for T in self.transactions:
			current_node = self.root
			for item,count in self.transactions[T]:
				current_node.add_child(item,count)
				current_node = current_node.children[item]
			
		
	
	
	def prune_tree(self):
		""" Prunes all the nodes in the tree below min_support by recursively calling prune_children starting with the root """
		#print "Pruning with min_support",self.min_support
		self.prune_subtree(self.root)
	
	def prune_subtree(self,node):
		""" Prunes all the nodes in the tree below min_support by recursively calling prune_children starting with the root """
		children_keys = node.children.keys()
		
		for child in children_keys:
			#self.prune_subtree(node.children[child])
			if node.children[child].count < self.min_support:
				node.delete_child(node.children[child].itemid)
			else:
				self.prune_subtree(node.children[child])
	
	def freq_comparator(self,x,y):
		return self.count[x[0]] - self.count[y[0]]
	
	def print_tree(self):
		self.print_tree_node(self.root, "")
	
	def print_tree_node(self,node,indent):
		if node is None:# or node.is_pruned==True:
			return
		""" Prints a bracketed representation of a tree"""
		print indent + "{ (" + str(node.itemid) + " : " + str(node.count) + ")"
		for c in node.children:
			self.print_tree_node(node.children[c], indent+"\t")
		print indent+"}"
	
	
	
	def mine_frequencies(self):
		fpm = SimpleFPMiner(self)
		freq_patterns = fpm.mine()
		return freq_patterns
		

# Imports #	
from simplefpminer import *

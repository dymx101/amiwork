

class FTree:
	''' Frequency Tree class ( similar to frequency pattern trees, but taking advantage of the specific structure of the given data ) 
		This class does not do pruning '''
	
	'''----------------------------------------------'''
	class FTreeNode:
		def __init__(self, itemid,tree,parent):
			self.itemid = itemid
			self.count = 0
			self.tree = tree
			self.parent = parent
			self.children = dict()	#need fast lookups
			
		
		def add_child(self, itemid,count=1):
			if self.children.get(itemid) is None:
				self.children[itemid] = FTree.FTreeNode(itemid, self.tree, self)
			self.children[itemid].count += count
			
		def child(self,itemid):
			return self.children.get(itemid)
		
	'''----------------------------------------------'''
	
	def __init__(self):
		self.root = None
		self.items = None
		self.fields = None
		
		self.frequency = None
		self.field_combo_cardinality = None
		self.max_freq = None
	
	def set_items(self,items):
		''' Takes a list of items. Stores them in self.items '''
		self.items = items
		
	def set_fields(self,fields):
		''' Takes a list of fields that the tree will be built upon. Order matters. Stores them in self.fields '''
		self.fields = fields
	
	def build(self):
		self.root = FTree.FTreeNode("root",self,None)
		for item in self.items:
			self.add_item(item)
	
	def add_item(self,item):
		self.root.count+= 1
		current_node = self.root
		for field in self.fields:
			val = getattr(item,field)
			current_node.add_child(val)
			current_node = current_node.child(val)
			
	
	def get_frequency_from_dict(self,query_dict):
		''' ---------------------------- '''
		def rec(qd,fields,at_field):
			if at_field == len(fields):
				return None
			
			tup = rec(qd,fields,at_field+1)
			if fields[at_field] in qd:
				prepend = ( qd[ fields[at_field] ] , )
				if tup is None:
					return prepend
			else:
				if tup is None:
					return None
				else:
					prepend = (None,)
				
			return prepend + tup
		''' ---------------------------- '''
		query_tuple = rec(query_dict,self.fields,0)
			
		return self.get_frequency_from_tuple(query_tuple)
	
	
	def get_frequency_from_tuple(self,tuple):
		if tuple in self.frequency:
			return self.frequency[tuple]
		else:
			return 0
	
	def get_field_combo_cardinality(self,query_fields):
		fields = []
		for field in self.fields:
			if field in query_fields:
				fields.append(field)
		ftuple = (fields[0],)
		for i in range(1,len(fields)):
			ftuple+= ( fields[i], )
		return self.field_combo_cardinality[ftuple]
	
	
	def get_max_freq(self, query_fields):
		ftuple = None
		for field in self.fields:
			if field in query_fields:
				if ftuple is None:
					ftuple = (field,)
				else:
					ftuple += (field,)
		return self.max_freq[ftuple]
	
	
	def compute_stats(self):
		''' Computes the maximum frequency and the cardinality of different combos of fields '''
		self.field_combo_cardinality = dict()	#Stores the maximum frequency for the given field tuple
		self.max_freq = dict()	#Stores the maximum frequency for the given field tuple
		for key in self.frequency:
			fkey = None
			i=0
			#Generate the key
			for attr in key:
				if attr is not None:
					if fkey is None:
						fkey = (self.fields[i],)
					else:
						fkey+= (self.fields[i],)
				i+= 1
			
			#update max_freq for the fields
			if fkey in self.max_freq:	# and fkey in self.field_combo_cardinality is implied
				self.field_combo_cardinality[fkey] += 1
				if  self.frequency[key] > self.max_freq[fkey]:
					self.max_freq[fkey] = self.frequency[key]
			else:
				self.field_combo_cardinality[fkey] = 1
				self.max_freq[fkey] = self.frequency[key]
			
		
	
	def mine_frequencies(self):
		''' 
			Generates frequencies of all possible combination of fields. Also does it damn fast since our tree is so well structured.
			Unlike the Frequency pattern tree which goes bottom-up, (I think this will still be correct if it ) goes top down.
		'''
		self.frequency = dict()
		for key in self.root.children:
			self.mine_down(self.root.children[key],self.frequency)
	
	def mine_down(self,current_node,parent_frequency):
		''' 
			creates a list of frequencies in the subtree. Also responsible for updating the global self.frequencies. 
			Could have been working in time almost linear to the number of combinations which exist if i knew any :C
		'''
		frequencies = dict()
		current_tup = (current_node.itemid,)
		#Get the frequencies of the subtree
		for key in current_node.children:
			self.mine_down(current_node.children[key],frequencies)
		
		#Add this to the frequencies
		subtree_keys = frequencies.keys()
		
		new_combo = current_tup	#Only tuples can be hashed
		frequencies[ new_combo ]= current_node.count
		
		#Add this to the global frequency_table
		if parent_frequency.get(new_combo) is None:
			parent_frequency[new_combo] = current_node.count
		else:
			parent_frequency[new_combo] += current_node.count
	
		for item in subtree_keys:
			freq = frequencies[item]
			
			if parent_frequency.get( ((None,)+item) ) is None:
				parent_frequency[(None,)+item] = freq
			else:
				parent_frequency[(None,)+item] += freq
			
			new_combo = current_tup + item
			
			frequencies[new_combo] = freq #Frequency the combo
			#Add this to the global frequency_table
			if parent_frequency.get(new_combo) is None:
				parent_frequency[new_combo] = freq
			else:
				parent_frequency[new_combo] += freq
			
		return frequencies
		
	
	def dict_merge(self,a,b):
		''' a = a+b '''
		for key in b:
			if key in a:
				a[key]+= b[key]
			else:
				a[key] = b[key]
	
	
	def manual_get_frequency(self,item,query_fields=None):
		if query_fields is None:
			avoid_fields = []
		else:
			avoid_fields = list()
			for field in self.fields:
				if field not in query_fields:
					avoid_fields.append(field)
		return self._manual_get_frequency(item,avoid_fields,self.fields)
		

	
	def _manual_get_frequency(self,item,avoid_fields, fields=None, start_at_field=0,  current_node=None):
		''' returns the count of the combination in the tree. item is of same type as passed. Fields must still be a prefix of self.fields (in order)'''
		if fields is None:
			fields = self.fields
		
		if current_node is None:
			current_node = self.root
		
		while start_at_field < len(fields):
			field = fields[start_at_field]
			if field in avoid_fields:
				#print field , "is in avoid_Fields"
				sum=0
				for child in current_node.children:	#Iterate over all children of this kind
					sum+= self._manual_get_frequency(item,avoid_fields,fields,start_at_field+1,current_node.children[child])
				return sum
			else:
				val = getattr(item,field)
				current_node = current_node.child(val)
				if current_node is None:	#Nothing of this combination. Base case 
					return 0
				start_at_field+=1
			
		return current_node.count
	
	
	def item_count(self):
		return self.root.count
	
	def print_tree(self):
		""" Prints a bracketed representation of this ftree"""
		self.print_tree_node(self.root, "")
		
	
	def print_tree_node(self,node,indent):
		""" Prints a bracketed representation of the subtree with root at node """
		if node is None:
			return
		print indent + "{ (" + str(node.itemid) + " : " + str(node.count) + ")"
		for c in node.children:
			self.print_tree_node(node.children[c], indent+"\t")
		print indent+"}"
		
	

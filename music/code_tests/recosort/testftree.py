from recommendationsorters.ftree import FTree

class Likes:
	def __init__(self,tup):
		self.person = tup[0]
		self.item = tup[1]
		self.avec = tup[2]


tup = [
	( "Krishnan", "Maggi", "Cheese"),
	( "Krishnan", "Maggi", "Egg"),
	( "Srinath", "Maggi", "Cheese"),
	( "Krishnan", "Coffee", "Sugar"),
	( "Srinath", "Coffee", "Milk"),
	( "Srinath", "Coffee", "Sugar"),
	( "Krishnan", "Maggi", "Sugar")
]

items = []
for t in tup:
	items.append(Likes(t))


ftree = FTree()
ftree.set_items(items)
ftree.set_fields( ["person","item","avec"] )
ftree.build()
ftree.print_tree()

ftree.mine_frequencies()
print ftree.frequency

#exit(0)

print ftree.manual_get_frequency( Likes( ("Krishnan","Maggi","Egg") ) )
print ftree.manual_get_frequency( Likes( ("Krishnan","Maggi","Egg") ), ["person","item"]  )

print ftree.manual_get_frequency( Likes( ("Srinath","Maggi","Egg") ))
print ftree.manual_get_frequency( Likes( ("Srinath","Maggi","Egg") ), ["person","item"] )

print ftree.manual_get_frequency( Likes( ("Srinath","Maggi","Cheese") ), [] )
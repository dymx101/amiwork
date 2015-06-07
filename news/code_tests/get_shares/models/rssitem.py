class RSSItem:
	def __init__(self,xml_obj):
		self.title = xml_obj.find('title').text
		self.time = xml_obj.find('pubDate').text
		self.link = xml_obj.find('link').text
		self.description = xml_obj.find('description').text
		self.category = xml_obj.find('category').text
		
	<title>Pakistan hangs 8 including three 1998 plane hijackers</title>
		<link>http://indianexpress.com/article/world/neighbours/pakistan-hangs-8-including-three-1998-plane-hijackers/</link>
		<comments>http://indianexpress.com/article/world/neighbours/pakistan-hangs-8-including-three-1998-plane-hijackers/#comments</comments>
		<pubDate>Fri, 29 May 2015 05:41:13 +0000</pubDate>
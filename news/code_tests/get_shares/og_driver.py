import xml.etree.ElementTree

from sys import argv as commandline_argv
from opengraphsharescraper import OpenGraphShareScraper

class DummyContent:
	def __init__(self,rss_item):
		self.title = rss_item.find('title').text
		self.url = rss_item.find('link').text
		self.engagement = None
	

if len(commandline_argv) < 2 :
	print "needs xml file as first argument."
	exit(1)

xml_filename = commandline_argv[1]
rss_root = xml.etree.ElementTree.parse( xml_filename ).getroot()

items = rss_root.find('channel').findall('item')
urls = dict()
content = list()
for rss_item in items:
	content.append(DummyContent(rss_item))

''' Here are the lines you need  '''
ogscraper = OpenGraphShareScraper()
ogscraper.set_content(content)
ogscraper.update_og_shares()

for url in ogscraper.og_shares:
	print url, ogscraper.og_shares[url]
	

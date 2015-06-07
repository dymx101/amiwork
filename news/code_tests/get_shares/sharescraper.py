import requests

import json
import xml.etree.ElementTree
from sys import argv as commandline_argv

class DummyContent:
	def __init__(self,rss_item):
		self.title = rss_item.find('title').text
		self.link = rss_item.find('link').text
		self.engagement = None
	

def query_facebook_social_likes(links):	
	def chunk(long_array,chunksize):
		for i in xrange(0, len(long_array), chunksize):
			yield long_array[i:i+chunksize]	

	batch = list()
	request_unit = {"method":"GET", "relative_url":None}
	for link in links:
		relative_url = "v2.3/?id=" + link + "&fields=og_object{engagement{count}},share"
		request_unit["relative_url"] = relative_url
		batch.append({"method":"GET","relative_url": relative_url})
	batches = list(chunk(batch,50))

	post_params = dict()
	post_params['access_token'] = "494994220569217|1OG6YypCV2pM3dIlAGOZdCM1TI0"

	engagement = dict()
	bodies = list()
	responses = list()
	for batch in batches:
		post_params['batch'] = json.dumps(batch)
		r = requests.post("https://graph.facebook.com",params=post_params)
		responses += json.loads(r.text)#, object_hook=_unicode_decode_dict)
	return responses

	

if len(commandline_argv) < 2 :
	print "needs xml file as first argument."
	exit(1)

xml_filename = commandline_argv[1]
rss_root = xml.etree.ElementTree.parse( xml_filename ).getroot()

items = rss_root.find('channel').findall('item')
links = dict()
for rss_item in items:
	content = DummyContent(rss_item)
	links[content.link] = content

responses = query_facebook_social_likes(links)
#print responses

for response in responses:
	body = json.loads(response["body"])#, object_hook=_unicode_decode_dict)
	link = body["id"]
	links[link].engagement = {"likes":body["og_object"]["engagement"]["count"] , "comments": body["share"]["comment_count"], "shares": body["share"]["share_count"] }
	
for link in links:
	content = links[link]
	print link, content.engagement 
	

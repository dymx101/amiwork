import requests

import json

from mockfileregistry import MockFileRegistry as MFR
from databaseinterface import DatabaseInterface

class OpenGraphShareScraper:
	'''-------------------------------------'''
	''' Static members '''
	urls_per_request = 20
	requests_per_batch = 50
	'''-------------------------------------'''
	''' class for quick performance '''
	class StoryId_Url_Shares:
		def __init__(self,story_id, url, shares):
			self.url = url
			self.story_id = story_id
			self.shares = shares
		
	'''-------------------------------------'''
	
	def __init__(self):
		self.urls = None
		self.og_shares = None
	
	def set_social_stories(self,social_stories):
		for story in social_stories:
			self.og_scores[story.url] = StoryId_Url_Shares(story.story_id, story.url, 0)
	
	def get_result(self):
		return self.og_shares
	
	
	def _unicode_decode_dict(self,data):
		'''---------------------------------------'''
		def _unicode_decode_list(data):
			rv = []
			for item in data:
				if isinstance(item, unicode):
					item = item.encode('utf-8')
				elif isinstance(item, list):
					item = _unicode_decode_list(item)
				elif isinstance(item, dict):
					item = _unicode_decode_dict(item)
				rv.append(item)
			return rv
		'''---------------------------------------'''
		rv = {}
		for key, value in data.iteritems():
			if isinstance(key, unicode):
				key = key.encode('utf-8')
			if isinstance(value, unicode):
				value = value.encode('utf-8')
			elif isinstance(value, list):
				value = _unicode_decode_list(value)
			elif isinstance(value, dict):
				value = _unicode_decode_dict(value)
			rv[key] = value
		return rv

	def _query_open_graph(self):
		def chunk(long_array,chunksize):
			for i in xrange(0, len(long_array), chunksize):
				yield long_array[i:i+chunksize]	
			
		
		request_unit = {"method":"GET", "relative_url":None}
		url_chunks = list(chunk(self.urls,urls_per_request))
		
		post_params = dict()
		post_params['access_token'] = "494994220569217|1OG6YypCV2pM3dIlAGOZdCM1TI0"
		
		self.og_shares = dict()
		for url_chunk in url_chunks:
			i=0
			batch = list()
			relative_url = "v2.3/?fields=share&ids="+ ','.join(url_chunk)
			#request_unit["relative_url"] = relative_url
			batch.append({"method":"GET","relative_url": relative_url})
			
		batches = chunk(batch,requests_per_batch)
			
		for batch in batches:
			post_params['batch'] = json.dumps(batch)
			r = requests.post("https://graph.facebook.com",params=post_params)
			batch_response = json.loads(r.text)#, object_hook=_unicode_decode_dict)
			
			
			for single_request_response in batch_response:	
				body = json.loads(single_request_response["body"])
				for url_key in body:
					self.og_shares[item["id"]].shares = body[url_key]["share"]["share_count"])
				
		return self.og_shares
		
	
	def update_og_shares(self):
		''' MOCK FOR NOW! '''
		#return self._mock_query_open_graph()
		return self._query_open_graph()
		
	def _load_from_db(self):
		database_interface = DatabaseInterface.get_shared_instance()
		dbi = database_interface.dbi
		
		dbi.commit()
		
		dbi.autocommit(True)
		
	
	def _store_in_db(self):
		database_interface = DatabaseInterface.get_shared_instance()
		dbi = database_interface.dbi
		dbi.autocommit(False)
		
		for url in self.og_shares:
			dbi.execute("INSERT INTO news_socialscore_opengraphgshares",)
		dbi.commit()
		
		dbi.autocommit(True)
			
			
	''' MOCK METHODS '''
	def _mock_query_open_graph(self):
		f = open(MFR.og_shares[MFR.iter_number],'r')
		if not f:
			print "FILE NOT FOUND"
			exit(1)
		
		lines = f.read().split("\n")
		self.og_shares = dict()
		for line in lines:
			fields = line.split("\t")
			self.og_shares[fields[1]] = int(fields[2])
		
		return self.og_shares
	

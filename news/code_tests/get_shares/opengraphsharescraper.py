import requests

import json

from mockfileregistry import MockFileRegistry as MFR
from config import Config	

class OpenGraphShareScraper:
	def __init__(self):
		self.urls = None
		self.og_shares = None
	
	def set_urls(self,urls):
		self.urls = urls
	
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
		urls_per_request = 20
		requests_per_batch = 50
		
		def chunk(long_array,chunksize):
			for i in xrange(0, len(long_array), chunksize):
				yield long_array[i:i+chunksize]	
			
		
		request_unit = {"method":"GET", "relative_url":None}
		url_chunks = list(chunk(self.urls,urls_per_request))
		
		post_params = dict()
		post_params['access_token'] = Config.facebook_app_token
		
		self.og_shares = dict()
		batch = list()
		for url_chunk in url_chunks:
			i=0
			
			relative_url = "v2.3/?fields=share&ids="+ ','.join(url_chunk)
			batch.append({"method":"GET","relative_url": relative_url})
		
		
		batches = chunk(batch,requests_per_batch)
		#og_log = open('og_scrape.log', 'a')	
		
		for batch in batches:
			post_params['batch'] = json.dumps(batch)
			r = requests.post("https://graph.facebook.com",params=post_params)
			batch_response = json.loads(r.text)#, object_hook=_unicode_decode_dict)
			
			#og_log.write(r.text)
			for single_request_response in batch_response:	
				body = json.loads(single_request_response["body"])
				for url_key in body:
					self.og_shares[body[url_key]["id"]] = body[url_key]["share"]["share_count"]
				
		
		return self.og_shares
		
	
	"""
	def _OLD_query_open_graph(self):
		def chunk(long_array,chunksize):
			for i in xrange(0, len(long_array), chunksize):
				yield long_array[i:i+chunksize]	
		
		batch = list()
		request_unit = {"method":"GET", "relative_url":None}
		for url in self.urls:
			relative_url = "v2.3/?id=" + url + "&fields=og_object{engagement{count}},share"
			request_unit["relative_url"] = relative_url
			batch.append({"method":"GET","relative_url": relative_url})
		
		batches = list(chunk(batch,50))
		
		post_params = dict()
		post_params['access_token'] = "494994220569217|1OG6YypCV2pM3dIlAGOZdCM1TI0"
		
		responses = list()
		for batch in batches:
			post_params['batch'] = json.dumps(batch)
			r = requests.post("https://graph.facebook.com",params=post_params)
			responses += json.loads(r.text)#, object_hook=_unicode_decode_dict)
		
		return responses
	"""
	def update_og_shares(self):
		''' MOCK FOR NOW! '''
		return self._query_open_graph()
		#return self._mock_query_open_graph()
		
	
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
	

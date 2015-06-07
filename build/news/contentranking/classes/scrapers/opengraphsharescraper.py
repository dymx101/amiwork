import requests, json


from ..localconfig import LocalConfig
from globalconfig import GlobalConfig

class OpenGraphShareScraper:
	''' Static vars '''
	urls_per_request = LocalConfig.opengraphscraper_urls_per_request
	requests_per_batch = LocalConfig.opengraphscraper_requests_per_batch
	
	def __init__(self):
		self.urls = None
		self.og_shares = None
	
	def set_urls(self,urls):
		''' urls: A list of urls to use as id while querying facebook's open graph ''' 
		self.urls = urls
	
	def get_result(self):
		''' Returns self.og_shares. You must have called update_og_shares before this for the result to exist '''
		return self.og_shares
	
	
	def update_og_shares(self):
		''' calls self._query_open_graph() and returns the result '''
		return self._query_open_graph()	
	
	
	def _query_open_graph(self):
		''' Queries facebook's open graph and populates self.og_shares. 
			og_shares is a dictionary of the form { url: share_count[,...] }
		The (number of urls per request) to send and the (number of such requests to be made per batch request) can be set in ../localconfig.py '''
		
		def chunk(long_array,chunksize):
			for i in xrange(0, len(long_array), chunksize):
				yield long_array[i:i+chunksize]	
			
		
		request_unit = {"method":"GET", "relative_url":None}
		url_chunks = list(chunk(self.urls,self.urls_per_request))
		
		post_params = dict()
		post_params['access_token'] = GlobalConfig.facebook_app_token
		
		self.og_shares = dict()
		batch = list()
		for url_chunk in url_chunks:
			i=0
			
			relative_url = "v2.3/?fields=share&ids="+ ','.join(url_chunk)
			batch.append({"method":"GET","relative_url": relative_url})
		
		
		batches = chunk(batch, self.requests_per_batch)
		#og_log = open('og_scrape.log', 'a')	
		
		for batch in batches:
			post_params['batch'] = json.dumps(batch)
			r = requests.post("https://graph.facebook.com",params=post_params)
			batch_response = json.loads(r.text)
			
			#og_log.write(r.text)
			for single_request_response in batch_response:	
				body = json.loads(single_request_response["body"])
				for url_key in body:
					self.og_shares[body[url_key]["id"]] = body[url_key]["share"]["share_count"]
				
		
		return self.og_shares
		
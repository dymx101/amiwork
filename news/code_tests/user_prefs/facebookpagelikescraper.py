from databaseinterface import DatabaseInterface
import requests,json

class FacebookPageLikeScraper:
	def __init__(self,user_access_token):
		self.user_access_token = user_access_token
		self.feed_ids = None					#{ "facebook_page_id": "feed_id_in_db" }
		self.liked_feed_ids = None				# List
	
	def load_feed_ids(self):
		dbi = DatabaseInterface.get_shared_instance()
		cursor = dbi.execute("SELECT feed_id,facebook_page_id FROM news_feeds WHERE facebook_page_id IS NOT NULL",None)
		rows = cursor.fetchall()
		self.feed_ids = dict()
		for row in rows:
			if row['facebook_page_id'] is None:
				continue
			self.feed_ids[row['facebook_page_id']] = row['feed_id']
		
	
	def get_liked_feed_ids(self):
		self._query_open_graph()
	
	def _query_open_graph(self):
		requests_per_batch = 50
		
		''' ------------------------------------------------ '''
		def chunk(long_array,chunksize):
			for i in xrange(0, len(long_array), chunksize):
				yield long_array[i:i+chunksize]	
		''' ------------------------------------------------ '''
		batch = list()
		for feed_page_id in self.feed_ids:
			relative_url = "v2.3/me/likes/"+str(feed_page_id)+'?fields=id'
			batch.append({"method":"GET","relative_url": relative_url})
		
		request_url = "https://graph.facebook.com/"
		post_params = dict()
		post_params['access_token'] = self.user_access_token
		
		batches = chunk(batch,requests_per_batch)
		self.liked_feed_ids = list()
		for batch in batches:
			post_params['batch'] = json.dumps(batch)
			r = requests.post("https://graph.facebook.com",params=post_params)
			batch_response = json.loads(r.text)
		
			for single_request_response in batch_response:	
				body = json.loads(single_request_response["body"])
				for obj in body["data"]:
					self.liked_feed_ids.append(self.feed_ids[ long(obj["id"]) ])
		
		return self.liked_feed_ids
	

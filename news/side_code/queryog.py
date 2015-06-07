import requests
import json
def _query_open_graph(urls):
		urls_per_request = 20
		requests_per_batch = 50
		
		def chunk(long_array,chunksize):
			for i in xrange(0, len(long_array), chunksize):
				yield long_array[i:i+chunksize]	
			
		
		request_unit = {"method":"GET", "relative_url":None}
		url_chunks = list(chunk(urls,urls_per_request))
		
		post_params = dict()
		post_params['access_token'] = "494994220569217|1OG6YypCV2pM3dIlAGOZdCM1TI0"
		
		scores = dict()
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
					scores[body[url_key]["id"]] = body[url_key]["share"]["share_count"]
			
			
		return scores
	
f = open('100links.txt','r')
urls = f.read().split("\n")
print _query_open_graph(urls)
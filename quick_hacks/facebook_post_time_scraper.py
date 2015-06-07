import requests,json,sys,time

if len(sys.argv) <2:
	print "Specify page_id as commandline argument "
	exit(1)


page_id = 'thehindu'
fields = 'id,created_time'
results_per_request = 100
how_far_back = 86400 * 14 		# 2 weeks

access_token= #Your access token here


''' Now the code. Don't touch shit below this line '''

start_url = "https://graph.facebook.com/%s/feed?fields=%s&limit=%s&access_token=%s"% (page_id,fields,results_per_request,access_token)

time_now = int(time.time())
earliest_time_so_far = time_now
url = start_url
kill_off_time = time_now - how_far_back

while earliest_time_so_far >= kill_off_time:
	response = requests.get(url)
	results = json.loads(response.text)
	
	for result in results["data"]:
		id = result["created_time"]
		created_time = result["id"]
		earliest_time_so_far = min(earliest_time_so_far, created_time )
		
		''' Handle it here '''
		print id,',',created_time
	
	url = results.paging.next
	
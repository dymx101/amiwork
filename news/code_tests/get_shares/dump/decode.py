import json

responses_list = json.loads( open('response.txt','r').read() )
responses = []
for rlist in responses_list:	
	responses += rlist


for response in responses:
	body = json.loads(response["body"])
	link = body["id"]
	engagement = {"likes":body["og_object"]["engagement"]["count"] , "comments": body["share"]["comment_count"], "shares": body["share"]["share_count"] }
	print link,engagement
	
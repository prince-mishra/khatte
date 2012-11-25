import json
import os
import urllib
def do():
	url 	= 'https://raw.github.com/prince-mishra/khatte/master/latest.json'
	f 		= urllib.urlopen(url)
	r 		= f.read()
	rjson 	= json.loads(r)
	for k in rjson['data']:
		likes = k.get('likes', 0)
		comments	= k.get('comments', 0)
		if likes and likes['count'] > 20:
			
			print likes['count'], '\t', comments['count'], '\n'	

def grab():
	group_id 		= '303471226332209'
	access_token 	= 'AAABbziNJcXsBAJJeJwuHh59l6FwAkeSIb0cRi0EbbT51QZCRSeBVkyJTAypxahixZCZBdGKtdBA4vT8Qr1QAd006nhjf5ypGRyLWjY1AQZDZD'
	url 			= 'https://graph.facebook.com/' + group_id + '/feed/?access_token=' + access_token
	r 				= urllib.urlopen(url)
	rjson			= json.loads(r.read())
	page  = 0
	count = 0
	max_page = 3
	while page < max_page:
		for item in rjson['data']:
			count += 1
		next_page = rjson['paging']['next']
		new_url = next_page + '&access_token=' + access_token
		r = urllib.urlopen(new_url)
		rjson = json.loads(r.read())
		page += 1
		print "loaded page", page, count, next_page



if __name__ == "__main__":
	grab()








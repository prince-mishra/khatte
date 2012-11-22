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

if __name__ == "__main__":
	do()








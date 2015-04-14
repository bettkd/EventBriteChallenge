#import eventbrite
import httplib2
import pprint
import json
import re

'''--------------'''
api_root = 'https://www.eventbriteapi.com'
version = 'v3'
token = 'BKKRDKVUVRC5WG4HAVLT'
url = '%s/%s/categories/?token=%s'%(api_root, version, token)
use_ID = 89307119205
app_key = 'EALW47FKIXFBTPNHEM'
content_type = 'json'

h = httplib2.Http(".cache")
resp, content = h.request(url, "GET")

cont = json.loads(content)

cat = cont['categories']

categs = ['Music', 'Fashion & Beauty', 'Science & Technology']


for categ in categs:
	for ct in cat:
		if ct['name'] == categ:
			#pprint.pprint(ct)
			pass
'''------------'''

api_root = 'https://www.eventbrite.com'
url = '%s/%s/event_search?category=%s&app_key=%s'%(api_root, content_type, "Music", app_key)

resp, content = h.request(url, "GET")
cont = json.loads(content)

#pprint.pprint(cont['events'][0]['summary'])
for i in range(1,3):
	print "++++++++++++++++++++"
	pprint.pprint('title: '+cont['events'][i]['event']['title'])
	pprint.pprint('description: '+cont['events'][i]['event']['description'])
	pprint.pprint('start_date: '+cont['events'][i]['event']['start_date'])
	pprint.pprint('end_date: '+cont['events'][i]['event']['end_date'])
	pprint.pprint(cont['events'][i]['event']['title'])
	pprint.pprint(cont['events'][i]['event']['venue'])
	print "=============="
#	pprint.pprint(c['events'])
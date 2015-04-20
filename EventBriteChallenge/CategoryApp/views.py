import httplib2
import pprint
import json
import re
from django.http import HttpResponse
from django.template import RequestContext, loader
content_type = 'json'
app_key = 'EALW47FKIXFBTPNHEM'
h = httplib2.Http(".cache")
token = 'BKKRDKVUVRC5WG4HAVLT'
version = 'v3'
categ = 'Music'

def index(request):
	event_list  = the_event()
	template = loader.get_template('index.html')
	context = RequestContext(request, {'event_list': event_list})
	return HttpResponse(template.render(context))

def category():
	version = 'v3'
	token = 'BKKRDKVUVRC5WG4HAVLT'
	url = 'https://www.eventbriteapi.com/%s/categories/?token=%s'%(version, token)
	use_ID = 89307119205

	
	resp, content = h.request(url, "GET")

	cont = json.loads(content)

	cat = cont['categories']

	categs = ['Music', 'Fashion & Beauty', 'Science & Technology']


	for categy in categs:
		for ct in cat:
			if ct['name'] == categy:
				#pprint.pprint(ct)
				pass
	'''------------'''
	print cat

def the_event():
	url = 'https://www.eventbrite.com/%s/event_search?category=%s&app_key=%s'%(content_type, categ , app_key)

	resp, content = h.request(url, "GET")
	cont = json.loads(content)

	#pprint.pprint(cont['events'][0]['summary'])

	event = {}
	event_list = []
	for i in range(1,11):
		title  = cont['events'][i]['event']['title']
		capacity = cont['events'][i]['event']['capacity']
		description = cont['events'][i]['event']['description']
		privacy = cont['events'][i]['event']['privacy']
		logo =cont['events'][i]['event'].get('logo_ssl')

		event_list.append(title)
		event_list.append(capacity)
		event_list.append(privacy)
		event_list.append(logo)
		'''
		#event_list.append(description) #invoked to see more details
		'''
		print "=============="
	#	pprint.pprint(c['events'])

	return event_list

	#return [1,3,4,5,3]

#category()
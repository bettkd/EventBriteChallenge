import httplib2
import pprint
import json
import re
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.defaulttags import register

@register.filter
def get_item(d, k):
    return d[k]

content_type = 'json'
app_key = 'EALW47FKIXFBTPNHEM'
h = httplib2.Http(".cache")
token = 'BKKRDKVUVRC5WG4HAVLT'
version = 'v3'
categ = 'Music'
descriptions = []

def index(request):
	titles, capacities, privacies, logos, venues  = the_event()
	count = [i for i in range(0,len(titles))]
	template = loader.get_template('index.html')
	context = RequestContext(request, {'event_list': [{'titles':titles, 'capacities':capacities, 'privacies':privacies, 'logos':logos, 'venues':venues, 'count':count}]})
	return HttpResponse(template.render(context))

def description(request):
	template = loader.get_template('description.html')
	context = RequestContext(request, {'descriptions':descriptions})
	print descriptions[0]
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

	titles = []
	capacities = []
	privacies = []
	logos = []
	venues = []
	for i in range(1,11):
		title  = cont['events'][i]['event']['title']
		capacity = cont['events'][i]['event']['capacity']
		description = cont['events'][i]['event']['description']
		privacy = cont['events'][i]['event']['privacy']
		logo = cont['events'][i]['event'].get('logo')
		address1 = cont['events'][i]['event']['venue']['address']
		city = cont['events'][i]['event']['venue']['city']
		region = cont['events'][i]['event']['venue']['region']
		country = cont['events'][i]['event']['venue']['country']
		venue = ', '.join([address1, city, region, country])

		titles.append(title)
		capacities.append(capacity)
		privacies.append(privacy)
		logos.append(logo)
		venues.append(venue)
		descriptions.append(description)
	#	pprint.pprint(c['events'])

	return titles, capacities, privacies, logos, venues


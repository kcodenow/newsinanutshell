from nian_auth import NIANAuthenticate
import requests

url = ('http://newsapi.org/v2/top-headlines?'
       'country=ie&'
       'apiKey=XOX')
response = requests.get(url).json()
status = response['status']

if(status == 'ok'):
	print('OK, fetching news ...' + '\n\n')
	articles = response['articles']
	for article in articles:
		print(article['title'] + '\n' + article['url'] + '\n')

quick_links={
	'everything': '',
	'uk_news': '',
	'uk_sports': '',
	'us_news': '',
	'us_sports': '',
}


URL_TOP_HEADLINES = 'https://newsapi.org/v2/top-headlines'

class NewsInANutshell(object):
	def __init__(self, api_key):
		self.auth() = NIANAuthenticate(api_key=api_key)

	def get_news(self, country=None, category=None, sources=None, q=None, page_size=None, page=1):
		fields={}

		# TODO - check valid strings
		# TODO - ensure country/category/sources are supported by NewsAPI
		if country is not None:
			fields['country']=country

		if category is not None:
			fields['category']=category

		if sources is not None:
			fields['sources']=sources

		if q is not None:
			fields['q']=q

		response = requests.get(URL_TOP_HEADLINES, auth=self.auth, params=fields)
		if response.status_code in [200, 201]:
			articles = response.json()['articles']
			for article in articles:
				print(article['title'] + '\n' + article['url'] + '\n')
		else:
			print(response.status_code + ' - response was not OK')
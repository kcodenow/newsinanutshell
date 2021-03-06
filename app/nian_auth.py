from requests.auth import AuthBase

class NIANAuthenticate(AuthBase):
	"""
	https://newsapi.org/docs/authentication
	"""
	def __init__(self, api_key):
		self.api_key = api_key

	def __call__(self, request):
		request.headers.update(get_auth_headers(self.api_key))

def get_auth_headers(api_key):
	return {"Content-Type": "Application/JSON", "Authorization": api_key}
import cookielib
import urllib
import urllib2
from bs4 import BeautifulSoup

def site_authverify(site_resp,error):
	result = False
	site_html = BeautifulSoup(site_resp.read())
	if site_html.find(text=str(error)) == None:
		result = True
	return result

def site_connect(site,u_field,username,p_field,password):
	result = 0

	# Store the cookies and create an opener that will hold them
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	# Install opener
	urllib2.install_opener(opener)

	# The action/ target from the form
	authentication_url = str(site)

	# Input parameters we are going to send
	payload = {str(u_field): str(username),str(p_field): str(password)}

	# Use urllib to encode the payload
	data = urllib.urlencode(payload)

	# Build  request object
	req = urllib2.Request(authentication_url, data)

	# Make the request
	resp = urllib2.urlopen(req)
	
	# Verify connection
	if(site_authverify(resp,"Login Error")):
		result = opener 

	#return opener
	return result

def site_crawl(url,opener):
	response = opener.open(str(url))
	return response



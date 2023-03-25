import requests, json
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def parse_main_articles(litem):
	litem_soup = BeautifulSoup(litem, "html.parser")
	
	h2_list = litem_soup.find_all("h2")
	
	h2_str = ''.join([str(item) for item in h2_list])
	
	h2_soup = BeautifulSoup(h2_str, "html.parser")
	
	a_list = h2_soup.find_all("a")
	
	headings = []
	for item in a_list:
		headings.append((item.get_text()).strip())
	
	###
	
	links = []
	for a in h2_soup.find_all('a', href=True):
	    links.append(a['href'])
	
	###
	
	articletext_list = litem_soup.find_all("div", {"class": "articletext"})
	
	articletext_str = ''.join([str(item) for item in articletext_list])
	
	articletext_soup = BeautifulSoup(articletext_str, "html.parser")
	
	images = []
	for img in articletext_soup.find_all('img', src=True):
		x = (img['src'])
		if ("data:image" in x):
			continue
		else:
			images.append(x)
	
	
	
	return([links, headings, images])



def main_request():
	response = requests.get("https://www.dailymail.co.uk/home/index.html")

	response.encoding = response.apparent_encoding
	
	main_soup = BeautifulSoup(response.text, "html.parser")

	puff_list = main_soup.find_all("div", {"class": "puff cleared"})

	luff = ''.join([str(item) for item in puff_list])
	
	litem_list = main_soup.find_all("div", {"itemtype": "//schema.org/ListItem"})
	
	litem = ''.join([str(item) for item in litem_list])

	main_articles = parse_main_articles(litem)

	luff_soup = BeautifulSoup(luff, "html.parser")

	li_list = luff_soup.find_all("li")

	li_str = ''.join([str(item) for item in li_list])

	li_soup = BeautifulSoup(li_str, "html.parser")

	###
	
	links = []
	for a in li_soup.find_all('a', href=True):
	    links.append(a['href'])

	###

	images = []
	for img in li_soup.find_all('img', src=True):
		x = (img['src'])
		if ("data:image" in x):
			continue
		else:
			images.append(x)

	###

	headings = []
	for heading in li_soup.find_all('strong'):
		headings.append((heading.get_text()).strip())

	main_links = main_articles[0]
	main_images = main_articles[2]
	main_headings = main_articles[1]

	for item in links:
		main_links.append(str(item))

	for item in images:
		main_images.append(str(item))

	for item in headings:
		main_headings.append(str(item))

	return([main_links, main_headings, main_images])



def fetch_homepage():
	x = (main_request())
	
	links = x[0]
	headings = x[1]
	images = x[2]
	
	increment = 0
	
	articles = []
	
	while True:
		try:
			w = []
			w.append(links[increment])
			w.append(headings[increment])
			w.append(images[increment])
			articles.append(w)
			increment += 1
		except:
			break
	
	
	return(json.dumps(articles))

def search_request(searchterm):
	url_safe_prompt = searchterm.replace(" ", "%20")
	
	url = ("https://www.dailymail.co.uk/home/search.html?sel=site&searchPhrase=" + url_safe_prompt)
	response = requests.get(url)
	
	response.encoding = response.apparent_encoding
	
	soup = BeautifulSoup(response.text, "html.parser")
	
	main_soup_list = soup.find_all("div", {"class": "sch-result"})
	
	main_soup_str = ''.join([str(item) for item in main_soup_list])
	
	main_soup = BeautifulSoup((str(main_soup_str)), "html.parser")
	
	h3_list = main_soup.find_all("h3")
	
	h3_str = ''.join([str(item) for item in h3_list])
	
	h3_soup = BeautifulSoup(h3_str, "html.parser")
	
	###
	
	links = []
	for a in h3_soup.find_all('a', href=True):
	    links.append(a['href'])
	
	###
	
	headings = []
	for heading in h3_soup.find_all('h3'):
		headings.append((heading.get_text()).strip())
	
	###
	
	images = []
	for img in main_soup.find_all('img', src=True):
		images.append(img['src'])
	
	return([links, headings, images])

def fetch_search(searchterm):
	x = search_request(searchterm)
	
	links = x[0]
	headings = x[1]
	images = x[2]
	
	increment = 0
	
	final = []
	
	while True:
		try:
			y = []
			y.append(links[increment])
			y.append(headings[increment])
			y.append(images[increment])
			final.append(y)
			increment += 1
		except:
			break
	
	return(json.dumps(final))

def fetch_article(url):
	response = requests.get(url)
	
	response.encoding = response.apparent_encoding
	
	soup = BeautifulSoup(response.text, "html.parser")
	
	article = (str(soup.find("div", {"itemprop": "articleBody"})))
	
	article_content_list = ((str(md(article))).splitlines())
	revised_content_list = []
	for item in article_content_list:
		item = ((str(item)).strip())
		if ("data:image" in item):
			continue
		else:
			if ("READ MORE" in item):
				continue
			else:
				revised_content_list.append(item.replace("‹ Slide me ›", ""))
	
	return('\n'.join(revised_content_list))

class DailyMail:
	'''Scrape data from the DailyMail and return in a JSON Format


 
 Current Functions:

 Fetch homepage:
 mail.homepage
 
 Search dailymail:
 mail.search("prompt here")
 
 Fetch specific article:
 mail.article("article url here")'''

	homepage = fetch_homepage()

	def search(self, query):
		'''Search dailymail with a prompt, results returned in a JSON format.'''
		self.searchresult = fetch_search(query)

	def article(self, article):
		'''Fetch an article identified by a URL in reading form, returned in a MARKDOWN format.'''
		self.articlecontent = fetch_article(article)
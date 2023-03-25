import requests, json
from bs4 import BeautifulSoup

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

class DailyMail:
	'''Scrape data from the DailyMail and return in a JSON Format'''

	homepage = fetch_homepage()
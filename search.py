import requests, json
from bs4 import BeautifulSoup

def search(searchterm):
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


x = search("budget")

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

with open("test.json", "w") as f:
	f.write((json.dumps(final)))
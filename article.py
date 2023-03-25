import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

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
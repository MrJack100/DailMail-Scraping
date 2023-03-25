import requests
from bs4 import BeautifulSoup

searchterm = ("budget")

url_safe_prompt = searchterm.replace(" ", "%20")

url = ("https://www.dailymail.co.uk/home/search.html?sel=site&searchPhrase=" + url_safe_prompt)
response = requests.get(url)

response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, "html.parser")

main_soup_list = soup.find_all("div", {"class": "sch-result"})

main_soup_str = ''.join([str(item) for item in main_soup_list])

main_soup = BeautifulSoup((str(main_soup_str)), "html.parser")

with open("testresponse.html", "w") as f:
	f.write((str(main_soup_str)))
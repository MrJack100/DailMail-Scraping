# DailMail-Scraping
Scrapes any DailyMail page and returns as a `JSON` format.

## Installation

No current way to install.


## Usage

How to get homepage contents.

```python
# Current way to import dailymail scraper
from dailymailclass import DailyMail

# Creates class
mail = DailyMail()

# Prints homepage articles
print(mail.homepage)

# Prints search results for "fire"
mail.search("fire")
print(mail.searchresult)

# Prints content of "https://www.dailymail.co.uk/news/article-11858277/HS2-created-ghost-towns-Britain-homeowners-forced-beloved-properties.html"
mail.article("https://www.dailymail.co.uk/news/article-11858277/HS2-created-ghost-towns-Britain-homeowners-forced-beloved-properties.html")
print(mail.articlecontent)
```
   
## Future Changes

- Add as a package to `PyPi`
- ~~Add all features~~ DONE
- Improve `JSON` format to instead have dictionaries, for example:

		[{"link":"https://example.com","heading":"HEADING HERE","image":"https://example.jpg"},{"link":"https://example.com","heading":"HEADING HERE","image":"https://example.jpg"}]
		
- ~~Think of more functions to add~~ DONE

## About

DailyMail is a mess, I'm creating this so I can turn it into a Flask API. I'm going to use that API as the backend for a website redesign.

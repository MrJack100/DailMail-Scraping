# DailMail-Scraping
Scrapes any DailyMail page and returns as a `JSON` format.

## Installation

No current way to install.


## Usage

How to get homepage contents.

    # Current way to import DailyMail Scraper
    from dailymailclass import DailyMail
    
    # Creates class
    mail = DailyMail()
    
    # Prints homepage
    print(mail.homepage)
    
## Future Changes

- Add as a package to `PyPi`
- Add all features
- Improve `JSON` format to instead have dictionaries, for example:

		[{"link":"https://example.com","heading":"HEADING HERE","image":"https://example.jpg"},{"link":"https://example.com","heading":"HEADING HERE","image":"https://example.jpg"}]
		
- Think of more functions to add

## About

DailyMail is a mess, I'm creating this so I can turn it into a Flask API. I'm going to use that API as the backend for a website redesign.

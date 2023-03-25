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
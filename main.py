# Current way to import dailymail scraper
from dailymailclass import DailyMail

# Creates class
mail = DailyMail()

# Prints homepage articles
print(mail.homepage)

# Prints search results for "fire"
mail.search("fire")
print(mail.searchresult)
from dailymailclass import DailyMail

mail = DailyMail()

with open("test.json", "w") as f:
	mail.search("fire")
	f.write(mail.searchresult)
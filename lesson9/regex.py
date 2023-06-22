import re

text = "Ini emailku : archel@gmail.com"

email_regex = "\w+@\w+\.\w+"

match = re.search(email_regex, text)
if match:
    print("Email ditemukan!")
    print(match.group())
else:
    print("Email tidak ditemukan!")

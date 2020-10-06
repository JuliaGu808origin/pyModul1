#  Write a Python program to get the dates 30 days before and after from the current date
# ！可以顯示再漂亮一點

import datetime

today = datetime.datetime.now()
before = today - datetime.timedelta(days=30)
after = today + datetime.timedelta(days=30)
print(f"Today: {today}, \n30 days before: {before}, \n30 days after: {after}")

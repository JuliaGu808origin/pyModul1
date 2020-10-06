import datetime
from datetime import timedelta

today = datetime.datetime.now()
for x in range(0,10):
    print(today.strftime("%Y-%m-%d"))
    today=today+timedelta(days=40)
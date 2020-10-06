import datetime
from datetime import timedelta

today = datetime.datetime(2016, 8, 20, 16, 18, 17)
newday=today+timedelta(days=40)
print(today.strftime("%m/%d/%Y %I:%M:%S %p"))
print(newday.strftime("%m/%d/%Y %I:%M:%S %p"))
print(newday.strftime("%A"))



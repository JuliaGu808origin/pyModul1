import datetime

today=datetime.datetime.now()
print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")
print(f"Hour: {today.hour}")
print(f"Minute: {today.minute}")
print(f"Second: {today.second}")
print(f"Millisecond: {today.microsecond/1000}")

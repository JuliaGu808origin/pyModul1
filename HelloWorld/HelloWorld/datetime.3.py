import datetime
import calendar

today=datetime.datetime.now()
print(today.strftime("%A"))
svensk={"Monday":"Måndag","Tuesday":"Tisday","Wednesday":"Onsday",
        "Thursday":"Torsdag","Friday":"Fredag","Saturday":"Lördag","Sunday":"Söndag"}
translate=list(filter(lambda each: each==today.strftime("%A"), svensk.keys()))
print(svensk[translate[0]])

demodayinweek=today.weekday()
demonameinweek=calendar.day_name[demodayinweek]
translate2=list(filter(lambda each: each==demonameinweek, svensk.keys()))
print(svensk[translate2[0]])



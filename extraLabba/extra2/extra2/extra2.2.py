#########################################################
# Write a Python program display a list of the dates 
# for the 2nd Saturday of every month for a given year.
#########################################################

import calendar

try:
    givenYear = int(input("Which year -> "))
except:
    print("Wrong year number !")
if givenYear:
    for month in range(1,13):
        eachMonth = calendar.monthcalendar(givenYear, month)
        first_sat_month = eachMonth[0]
        second_sat_month = eachMonth[1]
        third_sat_month = eachMonth[2]
        if first_sat_month[calendar.SATURDAY]: 
            saturday = second_sat_month[calendar.SATURDAY]
        else:
            saturday = third_sat_month[calendar.SATURDAY]
        print(f"{calendar.month_abbr[month]} {saturday}")

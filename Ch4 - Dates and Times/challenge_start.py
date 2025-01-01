# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

# Python code​​​​​​‌‌​​​‌‌​​​‌‌​‌‌​​‌‌‌​‌​​​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def count_days(year, month, whichday):
    # Your code goes here.
    count = 4
 
    # returns an array of weeks that represent the month
    cal = calendar.monthcalendar(year, month)
    # The first Friday has to be within the first two weeks
    # Check the 1st and 5th weeks
    weekone = cal[0]
    weekfive = cal[4]
   
    if weekone[whichday] != 0 and weekfive[whichday] != 0 :
        count = 5
    else:
        count = 4

    print("weekone weekfive whichday count", weekone, weekfive, whichday, count)
    return(count)     

    # You can edit this code to try different testing cases.
testyear = 2025
testmonth = 10
testday = 4
result = count_days(testyear, testmonth, testday)

result = count_days(testyear, testmonth, 0)
result = count_days(testyear, testmonth, 1)
result = count_days(testyear, testmonth, 2)
result = count_days(testyear, testmonth, 3)
result = count_days(testyear, testmonth, 4)
result = count_days(testyear, testmonth, 5)
result = count_days(testyear, testmonth, 6)

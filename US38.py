"""
US38
SSW 555
04/16/2022
"""

"""This is a program that checks the dates of a GEDCOM files
and lists the upcoming birthdays"""
from sys import builtin_module_names
from time import monotonic, strptime
import datetime
from dateutil.relativedelta import relativedelta

def formatDate(date):
    date = date.split()
    day = int(date[0])
    month = date[1]
    year = int(date[2])
    
    #Convert the month from text to number
    month = int(strptime(month,'%b').tm_mon)
    
    #format the date
    date = datetime.date(year, month, day)
    return date

def US38_ListUpcomingBirthDays(key, value):
    """This function lists the people with upcoming birthdays"""
    
    if 'BIRT' in value:
        birthday = value['BIRT']
        birthday = birthday.split()
        day = int(birthday[0])
        monthText = birthday[1]
        year = int(birthday[2])
        
        #Convert the month from text to number
        month = int(strptime(monthText,'%b').tm_mon)
        
        today = datetime.date.today()
        todayMonth = today.month
        todayDay = today.day
        
        if int(month) == int(todayMonth) and int(day) > int(todayDay):
            print("US38: Individual "+key+" has an upcoming birthday of "+monthText+" "+str(day))
        elif int(month) == int(todayMonth) + 1 and int(day) < int(todayDay):
            print("US38: Individual "+key+" has an upcoming birthday of "+monthText+" "+str(day))
        
        
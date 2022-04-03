"""
US13
SSW 555
04/03/2022
"""

"""This is a program that checks the dates of a GEDCOM files
and makes sure that siblings are not born too close together"""
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

def US13_SiblingSpacing(key, value, gedPeople):
    """This function checks to make sure that siblings are not born to close together"""
    
    if 'CHIL' in value:
        birthDays = []
        children = value['CHIL']
        for child in children:
            childBirthDate = formatDate(gedPeople[child]['BIRT'])
            birthDays.append(childBirthDate)

        for date1 in range(0, len(birthDays)):
            for date2 in range(date1+1, len(birthDays)):
                dateDiff = abs(birthDays[date2] - birthDays[date1])
                if int(dateDiff.days) >= 2 and int(dateDiff.days) < 248:
                    print("ERROR US13: Siblings are born too close together in family "+key)
        
        
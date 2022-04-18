"""
US35
SSW 555
04/13/2022
"""

"""This is a program checks individuals if they have been born within the last 30 days of the current date"""
from time import monotonic, strptime
import datetime

def US35_ListRecentBirths(key, value):
    """This is a program checks individuals if they have been born within the last 30 days of the current date"""
    
    #Get the current date
    today = datetime.date.today()
    
    #Sets difference duration of 30 days
    false_date = datetime.timedelta(days = 30)
    
    for tag in ['BIRT']:
        if tag in value:
            gedcomDate = value[tag]
            
            #Separate the day, month and year from the input
            gedcomDate = gedcomDate.split()
            day = int(gedcomDate[0])
            month = gedcomDate[1]
            year = int(gedcomDate[2])
            
            #Convert the month from text to number
            month = int(strptime(month,'%b').tm_mon)
            
            gedcomDate = datetime.date(year, month, day)
            
            #Calculates diff between today's date and birth date to find duration in days
            difference = today - gedcomDate
            
        if difference < false_date:
            print(key+" has been born within the last 30 days")
            
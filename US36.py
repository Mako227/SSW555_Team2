"""
US36
SSW 555
04/13/2022
"""

"""This is a program checks individuals if they have died within the last 30 days of the current date"""
from time import monotonic, strptime
import datetime

def US36_ListRecentDeaths(key, value):
    """This is a program checks individuals if they have died within the last 30 days of the current date"""
    
    #Get the current date
    today = datetime.date.today()
    
    #Sets difference duration of 30 days
    false_date = datetime.timedelta(days = 30)
    
    for tag in ['DEAT']:
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
            
            if tag == 'DEAT':
               death_date = gedcomDate
            
            #Calculates diff between today's date and death date to find duration in days
            difference = today - death_date
                
            if difference < false_date:
                print(key+" has died within the last 30 days")
   
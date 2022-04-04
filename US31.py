"""
US31
SSW 555
03/31/2022
"""

"""This is a program checks individuals if they are single age 30 and above"""
from time import monotonic, strptime
import datetime

def US31_ListLivingSingle(key, value):
    """This is a program checks individuals if they are single age 30 and above"""
    
    #Get the current date
    today = datetime.date.today()
    
    #Converts 30 years to 10,950 days
    false_date = datetime.timedelta(days = 10950)
    
    fams_found = False
    famc_found = False
    death_found = False
    
    for tag in ['FAMS']:
        if tag in value:
            fams_found = True
            
    for tag in ['FAMC']:
        if tag in value:
            famc_found = True
            
    for tag in ['DEAT']:
        if tag in value:
            death_found = True
            
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
            
            #Calculates diff between today's date and birth date to find duration of time alive in days (age)
            difference = today - gedcomDate
            
    if fams_found == False and famc_found == True and death_found == False:
        
        if difference > false_date:
            print(key+" was never married, is alive, and above 30 years of age")
        
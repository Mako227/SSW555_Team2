"""
US07
SSW 555
03/23/2022
"""

"""This is a program that checks the dates of a GEDCOM files
and makes sure the duration between birth and death dates, for dead 
people, and duration between the birth and current date, 
for living people, does not exceed 150 years"""
from time import monotonic, strptime
import datetime

def US07_LessThan150YearsOld(key, value):
    """This is a program that checks the dates of a GEDCOM files
and makes sure the duration between birth and death dates, for dead 
people, and duration between the birth and current date, 
for living people, does not exceed 150 years"""
    
    #Get the current date
    today = datetime.date.today()
    
    #Converts 150 years to 54,750 days
    false_date = datetime.timedelta(days = 54750)
    
    for tag in ['BIRT', 'DEAT']:
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
            
            #Calculates diff between today's date and birth date to find duration of time alive in days
            if tag == 'BIRT':
               birth_date = gedcomDate
               tag = 'BIRTH'
               difference = today - gedcomDate
               
               if difference > false_date:
                   print("ERROR US07: "+key+" exceeds 150 years being alive")
            
            #Calculates diff between death date and birth date to find duration of time lived in days      
            else:
                tag = 'DEATH'
                difference = gedcomDate - birth_date
                if difference > false_date:
                    print("ERROR US07: "+key+" was alive for more than 150 years")
                    
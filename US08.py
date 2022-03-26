"""
US08
SSW 555
03/24/2022
"""

"""This is a program that checks the dates of a GEDCOM files
and makes sure that a birthdate is not before the marriage date of their parents"""
from time import monotonic, strptime
import datetime

def US08_BirthBeforeMarriageParents(key, value, familyKey, familyValue):
    """This function checks to make sure the birth date is not before
    the marriage date of the parents"""
    if 'BIRT' in value:
        birth_date = value['BIRT']
        birth_date = birth_date.split()
        day = int(birth_date[0])
        month = birth_date[1]
        year = int(birth_date[2])
        
        #Convert the month from text to number
        month = int(strptime(month,'%b').tm_mon)
        
        #format the date
        birth_date = datetime.date(year, month, day)
        
    if 'MARR' in familyValue:
        marriage_date = familyValue['MARR']
        marriage_date = marriage_date.split()
        day = int(marriage_date[0])
        month = marriage_date[1]
        year = int(marriage_date[2])
        
        #Convert the month from text to number
        month = int(strptime(month,'%b').tm_mon)
        
        #format the date
        marriage_date = datetime.date(year, month, day)
    
    if birth_date < marriage_date:
        print("ERROR US08: Individual "+key+" birth date "+str(birth_date)+" occurs before the marriage date ("+str(marriage_date)+") of family "+familyKey)
    
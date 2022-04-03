"""
US10
SSW 555
04/03/2022
"""

"""This is a program that checks the dates of a GEDCOM files
and makes sure that the marriage date is 14 years after the birth date"""
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

def US10_MarriageAfter14(key, value, gedPeople):
    """This function checks to make sure the marriage date is at least 14 years
    after birth date"""
    
    if 'MARR' in value:
        husb_id = value['HUSB']
        wife_id = value['WIFE']
        husb_info = gedPeople[husb_id]
        wife_info = gedPeople[wife_id]
        husbBirth = formatDate(husb_info['BIRT'])
        wifeBirth = formatDate(wife_info['BIRT'])
        
        marrDate = formatDate(value['MARR'])
        
        husbMarrAge = marrDate.year-husbBirth.year
        wifeMarrAge = marrDate.year-wifeBirth.year
    
        
        if int(wifeMarrAge) < 14:
            print("ERROR US10: Individual "+wife_id+" was married at less than 14 years old")
        
        if int(husbMarrAge) < 14:
            print("ERROR US10: Individual "+husb_id+" was married at less than 14 years old")
        
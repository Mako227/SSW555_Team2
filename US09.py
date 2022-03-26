"""
US09
SSW 555
03/26/2022
"""

"""This is a program that checks the dates of a GEDCOM files
and makes sure that a birthdate is not after the death date of their parents"""
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

def US09_BirthBeforeParentsDeath(key, value, gedPeople, gedFamily):
    """This function checks to make sure the birth date is before
    the death date of the parents"""
    if 'FAMC' in value:
        birth_date = value['BIRT']
        birth_date = formatDate(birth_date)
        
        family = value['FAMC']
        familyInfo = gedFamily[family]
        
        if 'HUSB' in familyInfo:
            husbID = familyInfo['HUSB']
            husbInfo = gedPeople[husbID]
            
        if 'WIFE' in familyInfo:
            wifeID = familyInfo['WIFE']
            wifeInfo = gedPeople[wifeID]
        
        try:
            if 'DEAT' in husbInfo:
                husbDeath = husbInfo['DEAT']
                husbDeath = formatDate(husbDeath)
        except:
            #Husb not dead
            husbDeath = 'NULL'
        
        try:
            if 'DEAT' in wifeInfo:
                wifeDeath = wifeInfo['DEAT']
                wifeDeath = formatDate(wifeDeath)
        except:
            #Wife not dead
            wifeDeath = 'NULL'
            
        if wifeDeath != 'NULL':
            if birth_date > wifeDeath:
                print("ERROR US09: Individual "+key+" birth date "+str(birth_date)+" occurs after their mothers death ("+str(wifeDeath)+")")
        
        if husbDeath != 'NULL':
            if birth_date > (husbDeath + relativedelta(months=9)):
                print("ERROR US09: Individual "+key+" birth date "+str(birth_date)+" occurs more than 9 months after their fathers death ("+str(husbDeath)+")")
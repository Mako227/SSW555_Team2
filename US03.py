# -*- coding: utf-8 -*-
"""
US03
SSW 555
03/06/2022

"""
"""This is a program that checks the dates of a GEDCOM files
and makes sure the marriage date is not before the birth for each """
from time import monotonic, strptime
import datetime

def US03_BirthBeforeDeath(key, value):
    """This function checks to make sure the death is not
    before the birth of each individual"""
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
        
        if 'DEAT' in value:
            death_date = value['DEAT']
            death_date = death_date.split()
            day = int(death_date[0])
            month = death_date[1]
            year = int(death_date[2])
        
            #Convert the month from text to number
            month = int(strptime(month,'%b').tm_mon)
        
            #format the date
            death_date = datetime.date(year, month, day)
            
            if birth_date > death_date:
                print("ERROR US03: Individual "+key+" birth "+str(birth_date)+" occurs after the death of "+str(death_date))
# -*- coding: utf-8 -*-
"""
US02
SSW 555
03/06/2022
"""
"""This is a program that checks the dates of a GEDCOM files
and makes sure the marriage date is not before the birth of either spouse"""
from time import monotonic, strptime
import datetime

def US02_BirthBeforeMarriage(key, value, husb_info, wife_info):
    """This function checks to make sure the marriage date is not
    before the birth of either spouse"""
    if 'MARR' in value:
        marriage_date = value['MARR']
        marriage_date = marriage_date.split()
        day = int(marriage_date[0])
        month = marriage_date[1]
        year = int(marriage_date[2])
        
        #Convert the month from text to number
        month = int(strptime(month,'%b').tm_mon)
        
        #format the date
        marriage_date = datetime.date(year, month, day)
        
        #Get the birth date
        for info in [husb_info, wife_info]:
            if 'BIRT' in info:
                birth_date = info['BIRT']
                birth_date = birth_date.split()
                day = int(birth_date[0])
                month = birth_date[1]
                year = int(birth_date[2])

                #Convert the month from text to number
                month = int(strptime(month,'%b').tm_mon)

                #format the date
                birth_date = datetime.date(year, month, day)
            
                if marriage_date < birth_date:
                    if info['SEX'] == 'M':
                        member = 'husband'
                    else:
                        member = 'wife'
                    print("ERROR US02: Family "+key+" marriage date "+str(marriage_date)+" occurs beofore the birth of "+member+" "+str(birth_date))
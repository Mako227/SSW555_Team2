"""
US29
SSW 555
03/31/2022
"""

"""This is a program that checks if there is a death date for each individual in the GEDCOM file"""
#from time import monotonic, strptime
#import datetime

def US29_ListDeceased(key, value):
    """This is a program that checks if there is a death date for each individual in the GEDCOM file"""
    
    for tag in ['DEAT']:
        if tag in value:
            print(key+" is deceased")
            
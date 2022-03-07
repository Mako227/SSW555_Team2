"""
   File Name:    US12.py
   Authors:      Team 2
   Date:         7 Mar 2022
   Description:  Test US12 case
"""

# Need these for data storage
from typing import List, Dict
# For dealing with dates
from datetime import date, timedelta

MONTHS : dict = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
# Timedelta doesn't support "years" because leap years
SIXTY_YEARS  : timedelta = timedelta(days = 60*365)
EIGHTY_YEARS : timedelta = timedelta(days = 80*365)

def string_to_date(instring: str) -> date:
   """ Turn a GEDCOM-format date string into a datetime.date """
   # Split into sub-strings
   d = instring.split()
   # Convert to integers.
   # It could be DD MMM YYYY, or MMM YYYY, or just YYYY.  If necessary,
   # pad it out to DD MMM YYYY, using 28 Jun as the default because it's
   # approximately the middle of the year and every month >= 28 days.
   # THIS IS NOT AN IDEAL SOLUTION.
   if len(d) == 1:
      d = [28, 6, int(d[0])]
   elif len(d) == 2:
      d = [28, MONTHS[d[0]], int(d[1])]
   else:
      d = [int(d[0]), MONTHS[d[1]], int(d[2])]
   # Pass it to the date method in (y, m, d) order
   return date(d[2], d[1], d[0])
      

def US12_NoGeriatricParents(key, person, people, families):
   """ Verify plausible parent ages when each child is born """
   # Does this person have a family of origin and date of birth?
   if 'FAMC' in person.keys() and 'BIRT' in person.keys():
      # Record them
      child_date : date = string_to_date(person['BIRT'])
      family_id : str = person['FAMC']
      # Test mother's data
      if 'WIFE' in families[family_id].keys():
         mother_id = families[family_id]['WIFE']
         mom_date : date = string_to_date(people[mother_id]['BIRT'])
         if child_date - mom_date > SIXTY_YEARS:
            print('ANOMALY: INDIVIDUAL: US12: Mother ' + mother_id + ' was over 60 at birth of individual ' + key)
      # Test father's data
      if 'HUSB' in families[family_id].keys():
         father_id = families[family_id]['HUSB']
         dad_date : date = string_to_date(people[father_id]['BIRT'])
         if child_date - dad_date > EIGHTY_YEARS:
            print('ANOMALY: INDIVIDUAL: US12: Father ' + father_id + ' was over 80 at birth of individual ' + key)

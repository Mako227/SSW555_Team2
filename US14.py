"""
   File Name:    US14.py
   Authors:      Team 2
   Date:         28 Mar 2022
   Description:  Test US14 case
"""

# Need these for data storage
from typing import List, Dict

def US14_NoSextuplets(family_id, this_family, people):
   """ Verify that no family has more than five children with the same DoB """
   dates = list()
   tally : int = 0
   reportedList = []
   # Get all the dates of birth
   if 'CHIL' in this_family.keys():
      for child_id in this_family['CHIL']:
         dates.append(people[child_id]['BIRT'])
      # If there are more than 5, compare the dates
      if len(dates) > 5:
         for date in dates:
            tally = dates.count(date)
         if tally >= 5 and date not in reportedList:
            reportedList.append(date)
            print('ANOMALY: FAMILY: US14: Family ' + family_id + ' has ' + str(tally) + ' children with the same birthdate')
            return


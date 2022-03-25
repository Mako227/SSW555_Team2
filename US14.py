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
   # Get all the dates of birth
   if 'CHIL' in this_family.keys():
      for child_id in this_family['CHIL']:
         dates.append(people[child_id]['BIRT'])
      # If there are more than 5, compare the dates
      if len(dates) > 5:
         for date1 in dates:
            for date2 in dates:
               if date1 == date2:
                  tally = tally + 1
            if tally > 5:
               print('ANOMALY: FAMILY: US14: Family ' + family_id + ' has ' + str(tally) + ' children with the same birthdate')
               return
            # Clear the count for the next pass
            tally = 0


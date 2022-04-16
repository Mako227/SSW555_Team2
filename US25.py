"""
   File Name:    US25.py
   Authors:      Team 2
   Date:         15 Apr 2022
   Description:  Test US25 case
"""

# Need these for data storage
from typing import List, Dict

def US25_UniqueFirstNames(this_family, people):
   """ Verify that no two children in a family have the same first name """
   if 'CHIL' in this_family.keys():
      for child_id1 in this_family['CHIL']:
         # Get the name, divided by spaces into a list
         the_name = people[child_id1]['NAME'].split(' ')
         for child_id2 in this_family['CHIL']:
            # Don't compare people to themselves
            if child_id1 != child_id2:
               # Get the other name too
               other_name = people[child_id2]['NAME'].split(' ')
               # Compare just the first names
               if the_name[0] == other_name[0]:
                  print('ANOMALY: INDIVIDUAL: US25: Siblings ' + child_id1 + ' and ' + child_id2 + ' are both named ' + the_name[0])

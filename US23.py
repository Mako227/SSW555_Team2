"""
   File Name:    US23.py
   Authors:      Team 2
   Date:         8 Apr 2022
   Description:  Test US23 case
"""

# Need these for data storage
from typing import List, Dict

def US23_UniqueNameAndBirthdate(person_id, people):
   """ Verify that there are no duplicated name-and-birthdate combos """
   for current_id in people.keys():
      # Don't compare people to themselves
      if current_id != person_id:
         # Do the birthdates match?
         if people[current_id]['BIRT'] == people[person_id]['BIRT']:
            # Do the names match?
            if people[current_id]['NAME'] == people[person_id]['NAME']:
               print('ANOMALY: INDIVIDUAL: US23: IDs ' + current_id + ' and ' + person_id + ' have the same name and birthdate')

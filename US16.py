"""
   File Name:    US16.py
   Authors:      Team 2
   Date:         8 Apr 2022
   Description:  Test US16 case
"""

# Need these for data storage
from typing import List, Dict


def ExtractSurname(namestring : str) -> str:
   namestring_list = namestring.split('/')
   return namestring_list[1]

def US16_SharedSurname(family_id, this_family, people):
   """ Verify that all male members of the family have the same last name """
   # Who's your daddy?
   if 'HUSB' in this_family.keys():
      father_id : str = this_family['HUSB']
      father_surname : str = ExtractSurname(people[father_id]['NAME'])
   # If daddy is unknown, move on
   else:
      return
   # Check each of the children
   if 'CHIL' in this_family.keys():
      for child_id in this_family['CHIL']:
         # Male children only
         if people[child_id]['SEX'] == 'M':
            son_surname = ExtractSurname(people[child_id]['NAME'])
            if father_surname != son_surname:
               print('ANOMALY: INDIVIDUAL: US16: Male child ' + child_id + ' has different surname than father ' + father_id)

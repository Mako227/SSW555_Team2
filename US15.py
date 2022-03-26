"""
   File Name:    US15.py
   Authors:      Team 2
   Date:         28 Mar 2022
   Description:  Test US15 case
"""

# Need these for data storage
from typing import List, Dict

def US15_Under15Children(family_id, this_family):
   """ Verify that the family has fewer than 15 children total """
   # Get all the dates of birth
   if 'CHIL' in this_family.keys():
      if len(this_family['CHIL']) > 14:
         print('ANOMALY: FAMILY: US15: Family ' + family_id + ' has ' + str(len(this_family['CHIL'])) + ' children')

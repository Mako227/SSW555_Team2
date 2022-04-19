"""
   File Name:    US26.py
   Authors:      Team 2
   Date:         18 Apr 2022
   Description:  Test US26 case
"""

# Need these for data storage
from typing import List, Dict

def US26A_ConsistentEntries(this_person, people, families):
   """ Verify that individual entries agree with family records """
   # Is this person recorded as a child of some family?
   if 'FAMC' in people[this_person].keys():
      family_id = people[this_person]['FAMC']
      if this_person not in families[family_id]['CHIL']:
         print('ANOMALY: INDIVIDUAL: US26: Individual ' + this_person + ' not listed in claimed family of origin ' + family_id)
   # How about as a spouse in some family?
   if 'FAMS' in people[this_person].keys():
      # Could be a spouse in more than one family
      for family_id in people[this_person]['FAMS']:
         if people[this_person]['SEX'] == 'M':
            if this_person != families[family_id]['HUSB']:
               print('ANOMALY: FAMILY: US26: Individual ' + this_person + ' not listed as husband in claimed family ' + family_id)
         elif people[this_person]['SEX'] == 'F':
            if this_person != families[family_id]['WIFE']:
               print('ANOMALY: FAMILY: US26: Individual ' + this_person + ' not listed as wife in claimed family ' + family_id)


def US26B_ConsistentEntries(this_family, people, families):
   """ Verify that family entries agree with individual records """
   # Investigate the bona fides of each suspicious person in this suspicious family
   if 'HUSB' in families[this_family].keys():
      person_id = families[this_family]['HUSB']
      if person_id in people.keys():
         if this_family not in people[person_id]['FAMS']:
            print('ANOMALY: INDIVIDUAL: US26: Family ' + this_family + ' does not list individual ' + person_id + ' as husband as his record claims')
   if 'WIFE' in families[this_family].keys():
      person_id = families[this_family]['WIFE']
      if person_id in people.keys():
         if this_family not in people[person_id]['FAMS']:
            print('ANOMALY: INDIVIDUAL: US26: Family ' + this_family + ' does not list individual ' + person_id + ' as wife as her record claims')
   if 'CHIL' in families[this_family].keys():
      for person_id in families[this_family]['CHIL']:
         if person_id in people.keys():
            if this_family != people[person_id]['FAMC']:
               print('ANOMALY: INDIVIDUAL: US26: Family ' + this_family + ' does not list individual ' + person_id + ' as a child as his/her record claims')

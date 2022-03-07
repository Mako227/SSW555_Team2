"""
   File Name:    US11.py
   Authors:      Team 2
   Date:         7 Mar 2022
   Description:  Test US11 case
"""

# Need these for data storage
from typing import List, Dict
# For dealing with dates
from datetime import date

MONTHS : dict = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}

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
      

def US11_NoBigamists(key, person, people, families):
   """ Verify that there are no overlapping marriages """
   marriages : dict = dict()
   spousal_families : list = list()
   # Scrutinize this person for the crime of bigamy!
   # Remember, "key" is the person's ID and "person" is a Dict of their data
   # Get the list of all families they were a spouse in, if any
   if 'FAMS' in person.keys():
      spousal_families = person['FAMS']
      # If this person was in more than one marriage, did
      # each marriage end (in death or divorce) before the
      # next one began?
      if len(spousal_families) > 1:
         # Create records of all the marriages
         for fam_id in spousal_families:
            marriages[fam_id] = {}
            # Identify the spouse -- we're being very traditional here
            if person['SEX'] == 'M':
               spouse_id = families[fam_id]['WIFE']
            else:
               spouse_id = families[fam_id]['HUSB']
            marriages[fam_id]['spouse'] = spouse_id
            # When did the marriage start?
            marriages[fam_id]['start'] = string_to_date(families[fam_id]['MARR'])
            # Trickier question:  When did it end?
            if 'DIV' in families[fam_id].keys():
               marriages[fam_id]['end'] = string_to_date(families[fam_id]['DIV'])
            elif 'DEAT' in people[spouse_id]:
               marriages[fam_id]['end'] = string_to_date(people[spouse_id]['DEAT'])

         # Okay, that's all the marriages of record for this person.
         # Now compare the dates.
         for fam_id1 in spousal_families:
            for fam_id2 in spousal_families:
               # Don't compare a family to itself
               if fam_id1 != fam_id2:
                  if marriages[fam_id1]['start'] > marriages[fam_id2]['start'] and\
                     marriages[fam_id1]['start'] < marriages[fam_id2]['end']:
                     print('ANOMALY: INDIVIDUAL: US11: ' + key + ':  Married on '\
                           + str(marriages[fam_id1]['start']) + ' while still a spouse in family ' + fam_id1)

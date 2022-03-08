"""
Main file that will run all of the user stories
"""
from GedcomClass import Gedcom
from US01 import US01_DateBeforeCurrentDate
from US02 import US02_BirthBeforeMarriage
from US03 import US03_BirthBeforeDeath
from US05 import US05_MarriageBeforeDeath
from US11 import US11_NoBigamists
from US12 import US12_NoGeriatricParents

def Main():
    #set up the class based on an input file
    ged : Gedcom = Gedcom('/Users/tylermarchiano/Documents/Stevens/SSW555/Project/User Stories/amc.ged')
    individuals = ged.people.keys()
    families = ged.families.keys()
    
    #Run US01
    #Need to check all dates so need to check individuals and families
    for person in individuals:
        key = person
        value = ged.people[person]
        dateTags = ['BIRT', 'DEAT', 'DIV','MARR']
        US01_DateBeforeCurrentDate(key, value)
    
    for family in families:
        key = family
        value = ged.families[family]
        dateTags = ['BIRT', 'DEAT', 'DIV','MARR']
        US01_DateBeforeCurrentDate(key, value)
    
    #Run US02
    #Only Marriage date matters so can just check families
    for family in families:
        key = family
        value = ged.families[family]
        husb_id = value['HUSB']
        wife_id = value['WIFE']
        husb_info = ged.people[husb_id]
        wife_info = ged.people[wife_id]
        US02_BirthBeforeMarriage(key, value, husb_info, wife_info) 
     
    #Run US03
    #Need to check all dates so need to check individuals
    for person in individuals:
        key = person
        value = ged.people[person]
        dateTags = ['BIRT', 'DEAT']
        US03_BirthBeforeDeath(key, value)
    
    #Run US05
    #Only Marriage date matters so can just check families
    for family in families:
        key = family
        value = ged.families[family]
        husb_id = value['HUSB']
        wife_id = value['WIFE']
        husb_info = ged.people[husb_id]
        wife_info = ged.people[wife_id]
        US05_MarriageBeforeDeath(key, value, husb_info, wife_info)

    # Run US11
    for person in individuals:
        key = person
        value = ged.people[person]
        US11_NoBigamists(key, value, ged.people, ged.families)

    # Run US12
    for person in individuals:
        key = person
        value = ged.people[person]
        US12_NoGeriatricParents(key, value, ged.people, ged.families)

Main()

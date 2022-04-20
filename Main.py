"""
Main file that will run all of the user stories
"""
from GedcomClass import Gedcom
from US01 import US01_DateBeforeCurrentDate
from US02 import US02_BirthBeforeMarriage
from US03 import US03_BirthBeforeDeath
from US05 import US05_MarriageBeforeDeath
from US07 import US07_LessThan150YearsOld
from US08 import US08_BirthBeforeMarriageParents
from US09 import US09_BirthBeforeParentsDeath
from US10 import US10_MarriageAfter14
from US11 import US11_NoBigamists
from US12 import US12_NoGeriatricParents
from US13 import US13_SiblingSpacing
from US14 import US14_NoSextuplets
from US15 import US15_Under15Children
from US16 import US16_SharedSurname
from US18 import US18_SiblingsShouldNotMarry
from US21 import US21_CorrectGenderForRole
from US23 import US23_UniqueNameAndBirthdate
from US25 import US25_UniqueFirstNames
from US26 import *
from US29 import US29_ListDeceased
from US31 import US31_ListLivingSingle
from US35 import US35_ListRecentBirths
from US36 import US36_ListRecentDeaths
from US38 import US38_ListUpcomingBirthDays

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
    
    #Run US07
    #Only birth and death dates matter so can just check individuals
    for person in individuals:
        key = person
        value = ged.people[person]
        dateTags = ['BIRT', 'DEAT']
        US07_LessThan150YearsOld(key, value)
    
    #Run US08
    for person in individuals:
        key = person
        value = ged.people[person]
        if 'FAMC' in value:
            family = value['FAMC']
            familyInfo = ged.families[family]
            US08_BirthBeforeMarriageParents(key, value, family, familyInfo)
    
    #Run US09
    for person in individuals:
        key = person
        value =ged.people[person]
        US09_BirthBeforeParentsDeath(key, value, ged.people, ged.families)
        
    #Run US10
    for family in families:
        key = family
        value = ged.families[family]
        US10_MarriageAfter14(key, value, ged.people)

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
    
    #Run US13
    for family in families:
        key = family
        value = ged.families[family]
        US13_SiblingSpacing(key, value, ged.people)
    
    # Run US14
    for family_id in families:
        US14_NoSextuplets(family_id, ged.families[family_id], ged.people)
    
    # Run US15
    for family_id in families:
        US15_Under15Children(family_id, ged.families[family_id])
    
    # Run US16
    for family_id in families:
        US16_SharedSurname(family_id, ged.families[family_id], ged.people)
    
    #Run US18
    for family in families:
        key = family
        value = ged.families[family]
        US18_SiblingsShouldNotMarry(key, value, ged.people, ged.families)
        
    #Run US21
    #Need info from families to get gender info from individual husband and wife info
    for family in families:
        key = family
        value = ged.families[family]
        husb_id = value['HUSB']
        wife_id = value['WIFE']
        husb_info = ged.people[husb_id]
        wife_info = ged.people[wife_id]
        US21_CorrectGenderForRole(key, value, husb_info, wife_info, husb_id, wife_id)
    
    # Run US23
    for person in individuals:
        US23_UniqueNameAndBirthdate(person, ged.people)
    
    # Run US25
    for family_id in families:
        US25_UniqueFirstNames(ged.families[family_id], ged.people)

    # Run US26
    for person_id in individuals:
        US26A_ConsistentEntries(person_id, ged.people, ged.families)
    for family_id in families:
        US26B_ConsistentEntries(family_id, ged.people, ged.families)
    
    #Run US29
    #Only death dates matter so can just check individuals
    for person in individuals:
        key = person
        value = ged.people[person]
        dateTags = ['DEAT']
        US29_ListDeceased(key, value)
        
    #Run US31
    #Need to check individuals if they are single (never married) and above age 30 
    for person in individuals:
        key = person
        value = ged.people[person]
        dateTags = ['BIRT', 'DEAT', 'FAMS', 'FAMC']
        US31_ListLivingSingle(key, value)
        
    #Run US35
    #Need to check birth dates of individuals
    for person in individuals:
        key = person
        value = ged.people[person]
        dateTags = ['BIRT']
        US35_ListRecentBirths(key, value)
          
    #Run US36
    #Need to check death dates of individuals
    for person in individuals:
        key = person
        value = ged.people[person]
        dateTags = ['DEAT']
        US36_ListRecentDeaths(key, value)  
        
    #Run US38
    for person in individuals:
        key = person
        value = ged.people[person]
        US38_ListUpcomingBirthDays(key, value)
    
           
Main()

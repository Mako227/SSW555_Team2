"""
US18
SSW 555
04/16/2022
"""

"""This is a program that checks the contents of GEDCOM files
and makes sure that siblings are not married to each other"""

def US18_SiblingsShouldNotMarry(key, value, gedPeople, gedFamily):
    """This function checks to make sure that siblings are not married to each other"""
    if 'CHIL' in value:
        siblings = value['CHIL']
        for currentSibling in siblings:
            siblingValue = gedPeople[currentSibling]
            if 'FAMS' in siblingValue:
                marriedFamilies = siblingValue['FAMS']
                for fam in marriedFamilies:
                    familyValue = gedFamily[fam]
                    if familyValue['HUSB'] == currentSibling:
                        spouse = familyValue['WIFE']
                    elif familyValue['WIFE'] == currentSibling:
                        spouse = familyValue['HUSB']
                    
                    if spouse in siblings:
                        print("ERROR US18: Individual "+currentSibling+" is married to their sibling "+spouse)
        
        
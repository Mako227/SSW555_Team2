# -*- coding: utf-8 -*-
"""
US21
SSW 555
03/24/2022
"""
"""This is a program that checks the husband in a family should be male 
and the wife in a family should be female of a GEDCOM file"""

def US21_CorrectGenderForRole(key, value, husb_info, wife_info, husb_id, wife_id):
    """This is a program that checks the husband in a family should be male 
and the wife in a family should be female of a GEDCOM file"""
    
    #Set the bool flags to false for variable initialization
    found_wife : bool = False
    found_husb : bool = False
    
    #Sets the bool flag for husb to true if husb gender info has correct gender of male
    for info in [husb_info]:
            if info['SEX'] == 'M':
                found_husb = True
    #Sets the bool flag for wife to true if wife gender info has correct gender of female           
    for info in [wife_info]:
            if info['SEX'] == 'F':
                found_wife = True
                
    #Sets error off if any of the flag variables returns false           
    if found_husb == False:
        print("ERROR US21: Husband "+str(husb_id)+" in family "+str(key)+" is not the correct gender of male")
        
    if found_wife == False:
        print("ERROR US21: Wife "+str(wife_id)+" in family "+str(key)+" is not the correct gender of female")
         
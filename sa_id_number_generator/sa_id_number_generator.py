'''
Created on 30 December 2022

Created for QA purposes to aid testing of systems that require valid South African
Identity Numbers.

Functions:
    - generate_sa_id(date_of_birth, gender, citizen_status)
      Keyword arguments:
          date_of_birth (str) -- DOB in format YYYY-MM-DD. Also accepts adult, minor
                                and any. (Default: any)
          gender (str) -- male, female or any. (Default: any)
          citizen_status (str) -- citizen, resident or any (Default: any)
      Returns:
          list -- Returns string with generated South African ID number
                  Returns string with Date Of Birth
               -- Error is returned if the function is called incorrectly

Usage: Can be run as a standalone script, called directly or imported in other programs.

@author: Taahirj
'''

from datetime import datetime, date
from random import randint

def generate_sa_id(date_of_birth = "any", gender = "any", citizen_status = "any") -> list:
    # Variables
    checkdigit_sum = 0
    dob = ""
    sa_id_number = ""
    
    # Checks, creates and handles errors for the date of birth portion of the id number
    try:
        if str(date_of_birth).lower() == "minor":
            date_of_birth = str(randint(datetime.now().year - 16,datetime.now().year - 1)) + "-" + str(randint(1,12)).zfill(2) + "-" + str(randint(1,28)).zfill(2)
        if str(date_of_birth).lower() == "adult":
            date_of_birth = str(randint(datetime.now().year - 60,datetime.now().year - 19)) + "-" + str(randint(1,12)).zfill(2) + "-" + str(randint(1,28)).zfill(2)
        if str(date_of_birth).lower() == "any":
            date_of_birth = str(randint(datetime.now().year - 60,datetime.now().year - 1)) + "-" + str(randint(1,12)).zfill(2) + "-" + str(randint(1,28)).zfill(2)
        dob = date.fromisoformat(str(date_of_birth))
        sa_id_number = str(dob)[2:4] + str(dob)[5:7] + str(dob)[8:10]
    except Exception as e:
        return ["Invalid date of birth selected. Please specify date of birth in format YYYY-MM-DD. You may also specify 'minor', 'adult' or 'any' for random selection based on appropriate age requirements. Exact reason - " + str(e)]
    
    # Checks, creates and handles errors for the gender portion of the id number
    if str(gender).lower() == "female":
        sa_id_number = sa_id_number + str(randint(1,4999)).zfill(4)
    elif str(gender).lower() == "male":
        sa_id_number = sa_id_number + str(randint(5000,9999)).zfill(4)
    elif str(gender).lower() == "any":
        sa_id_number = sa_id_number + str(randint(1,9999)).zfill(4)
    else:
        return ["Invalid gender selected, please specify 'male', 'female' or 'any'"]
    
    # Checks, creates and handles the citezenship portion of the id number
    if str(citizen_status) == "citizen":
        sa_id_number = sa_id_number + "0"
    elif str(citizen_status) == "resident":
        sa_id_number = sa_id_number + "1"
    elif str(citizen_status) == "any":
        sa_id_number = sa_id_number + str(randint(0,1))
    else:
        return ["Invalid citizen status selected, please specify 'citizen', 'resident' or 'any'"]
    
    # Require an '8' in id number. Was used until 1980 to classify race but is constant since then
    sa_id_number = sa_id_number + "8"
    
    # Begin Luhn Algorithm - Checksum Creation
    try:
        for i in range(len(sa_id_number)):
            if i == 0 or i == 2 or i == 4 or i == 6 or i == 8 or i == 10:
                checkdigit_sum = checkdigit_sum + int(sa_id_number[i])
            else:
                temp = int(sa_id_number[i]) * 2
                if temp > 9:
                    temp = temp - 9
                checkdigit_sum = checkdigit_sum + temp
        checkdigit_sum = checkdigit_sum * 9
        sa_id_number = sa_id_number + str(checkdigit_sum)[2:]
    except Exception as e:
        return ["Unable to generate Luhn checksum. Please update parameters and try again."]
    
    # Return South African Identity Number 
    return [sa_id_number, dob.isoformat()]

if __name__ == '__main__':
    from optparse import OptionParser
    
    # Set up possible command line options
    usage = "Usage: python3 %prog [option1] arg1 [option2] arg2 ..."
    parser = OptionParser(usage=usage, version="%prog 1.0", description="Generates South African ID Numbers based on options specified. If no options are specified then options marked with (default) will be used.", epilog="Created by Taahirj to help with QA testing scenarios that require valid South African ID Numbers.")
    parser.add_option("-d", "--date_of_birth", action="store", type="string", dest="date_of_birth", help="DOB in format YYYY-MM-DD - Also accepts adult, minor or any: any (default)", default="any")
    parser.add_option("-g", "--gender", action="store", type="string", dest="gender", help="Gender with valid values as male, female or any: any (default)", default="any")
    parser.add_option("-c", "--citizen_status", action="store", type="string", dest="citizen_status", help="Citizen status with valid values as citizen, resident or any: any (default)", default="any")
    parser.add_option("-l", "--loops", action="store", type="int", dest="loops", help="Loops to the value N (number of ID Numbers to generate): 1 (default)", default=1)
    
    (options, args) = parser.parse_args()
    
    date_of_birth = options.date_of_birth
    gender = options.gender
    citizen_status = options.citizen_status
    loops = options.loops
    
    print("  ------------------------------------------------------------------------------");
    print(" | Identity Number  | Gender  | Type   | Date of Birth  | Age  | Citizen Status |");
    print("  ------------------------------------------------------------------------------");
    for loop in range(loops):
        # Returns id number generated
        current_sa_id = generate_sa_id(date_of_birth = date_of_birth,gender = gender,citizen_status = citizen_status)
        current_date_of_birth = current_sa_id[1]
        current_gender = "female" if int(current_sa_id[0][6:10]) < 5000 else "male"
        current_citizen_status = "citizen" if int(current_sa_id[0][10:11]) == 0 else "resident"
        current_age = int((datetime.now().date()-date.fromisoformat(current_sa_id[1])).days / 365.25)
        current_type = "minor" if current_age < 18 else "adult"
        print(f" | {current_sa_id[0]}    | {current_gender.ljust(6)}  | {current_type}  | {current_date_of_birth.ljust(10)}     | {str(current_age).rjust(2)}   | {current_citizen_status.ljust(8)}       |");
    print("  ------------------------------------------------------------------------------");

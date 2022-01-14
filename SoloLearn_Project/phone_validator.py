import re
#your code goes here
number=input()
pattern=r'^(1|8|9)(\d{7}$)'
def phone_validator(number):
    if re.search(pattern,number):
        return("Valid")
    else:
        return("Invalid")
print(phone_validator(number))

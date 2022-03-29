#!/usr/bin/env python3
def validate_user(username,minlen):
    assert type(username)==str, "UserName must be a string"
    if minlen<1:
        raise ValueError("minlen must be greater than one")
    if len(username)<minlen:
        return False
    if not username.isalnum():
        return False
    return True
print(validate_user("john",6)) #False
print(validate_user("JohnAssebe",6)) #True
print(validate_user(1,2)) #raise an assertion error



import re
pattern=r'^[a-zA-z_][a-zA-z0-9_]*$'
def is_valid(txt):
    return re.search(pattern,txt)!=None
print(is_valid("_valid_variable_name")) #True
print(is_valid("9invalid")) #False

def format_address(address_string):
  # Declare variables
  addresses=address_string.split()
  street_name=''
  # Separate the address string into parts
  # Traverse through the address parts
  for address in addresses:
    # Determine if the address part is the
    # house number or part of the street name
    if address.isdigit():
      house_number=address
    else:
      street_name+=' '+address
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number,street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

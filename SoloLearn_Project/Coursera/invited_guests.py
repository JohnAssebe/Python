def combine_guests(guests1, guests2):
  combined={}
  for rory_guest in guests1.keys():
    if rory_guest not in guests2.keys():
      combined[rory_guest]=[guests1[rory_guest],0]
    else:
      combined[rory_guest]=[guests1[rory_guest],guests2[rory_guest]]
  for Taylors_guest in guests2.keys():
    if Taylors_guest not in guests1.keys():
      combined[Taylors_guest]=[0,guests2[Taylors_guest]]
  return combined

  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

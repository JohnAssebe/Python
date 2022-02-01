def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    new_wrd=""
    if len(word)>1:
        first_letter=word[0]
        say+=word[1:]+first_letter+"ay "
    # Turn the list back into a phrase
  return say
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay inay ythonpay siay unfay"

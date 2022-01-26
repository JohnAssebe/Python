def is_palindrome(input_string):
	# We'll create two strings, to compare them
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string[::-1]:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
		if len(input_string)>1:
			reverse_string +=letter
	# Compare the strings
	input_string=input_string.replace(" ","").lower()
	reverse_string=reverse_string.replace(" ","").lower()
	if input_string==reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

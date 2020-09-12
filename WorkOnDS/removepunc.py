"""
@Author:Yohannes Assebe(John Assebe)
"""
def remove_punc(sentence):
	try:
		new_sent=""
		if len(sentence)<=1 | sentence.isalpha():
			return  sentence
		else:
			for char in sentence:
				if char.isalpha() | char.isspace():
					new_sent+=char
			return new_sent
	except(Exception) as err:
		print("Something Wrong Happen  "+ str(err))
print(remove_punc("Let's Try, John"))

"""
@Author:Yohannes Assebe(John Assebe) 
"""
from collections import Counter
def word_counter(sentence):
	if len(sentence)<=1:
		return sentence
	else:
		word_counter=Counter()
		word_counter.update(sentence.strip().split(" "))
		return word_counter

for key,value in word_counter("John Assebe square word_counter John").items():
	print(key,value)		

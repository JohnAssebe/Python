from matplotlib import pyplot as plt
from collections import Counter
# print(help(dict))
class CharacterFrequency:
	def __init__(self,file_name):
		self._file=file_name
	def plot(self):
		chars=Counter()
		try:
			with open(self._file) as file:
				for char in file.read():
					chars.update(char)
		except(Exception) as err:
			print("File Not Found"+str(err))

		for key,value in chars.most_common(15):
		    plt.style.use("ggplot")
		    plt.barh(key,value)
		    plt.title("Draw Characters of file")
		    plt.ylabel("Alphabets")
		    plt.xlabel("Frequency")
		return plt.show() 
CharacterFrequency("go1.7.txt").plot()



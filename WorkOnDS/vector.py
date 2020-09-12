class Vector:
	def __init__(self,dim):
		self._coord=[0]*dim
	def __len__(self):
		return len(self._coord)
	def __getitem__(self,j):
		return self._coord[j]
	def __setitem__(self,j,val):
		self._coord[j]=val
	def __add__(self,other):
		if len(self)!=len(other):
			return "Size unmatch"
		else:
			result=Vector(len(self))
			for i in range(len(self)):
				result[i]=self[i]+other[i]
			return result
	def __eq__(self,other):
		return self._coord==other._coord
	def __ne__(self,other):
		return not self==other
	def __str__(self):
		return "<"+str(self._coord[0:])+">"

if __name__=="__main__":
	vec1=Vector(5)
	print(len(vec1))
	print(vec1)
	for i in range(len(vec1)):
		vec1[i]=i
	print(vec1)
	vec2=Vector(5)
	for i in range(len(vec2)):
		vec2[i]=i+5
	print(vec2)
	print(vec1+vec2)
	print(vec1==vec2)
	print(vec1!=vec2)
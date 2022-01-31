def skip_elements(elements):
	new_lst=[]
	for index,element in enumerate(elements):
		if index%2==0:
			new_lst.append(element)
	return new_lst

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

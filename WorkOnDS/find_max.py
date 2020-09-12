def find_max(lst):
	try:
		max_num=lst[0]
		for item in lst:
			if item>max_num:
				max_num=item
		return max_num
	except(Exception) as err:
		return "Something wrong :",str(err)

print(find_max([i for i in range(10000011)]))
import os
def disk_usage(path):
	total=os.path.getsize(path)
	if os.path.isdir(path):
		for filename in os.listdir(path):
			child_path=os.path.join(path,filename)
			total+=disk_usage(child_path)
	print ("{0:1}" .format(total), path)
	return total
print(disk_usage('C:\\Users\\User1\\Desktop\\PythonPractice\\Book'))
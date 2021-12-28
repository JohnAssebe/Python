import copy
print("This is not the way of copy")

list1=[1,2,3,4]
list2=list1
list2.append(3)
# This is not the way of copy
print(list1)
print(list2)


# Shallow Copy

list3=copy.copy(list1)
list3.append(5)
print()
print("shallow copy")
print(list1)
print(list3)


# Deep Copy (more prefferable)

print()
print("Deep copy")
print(list1)
list4=copy.deepcopy(list1)
list4.append(5)
print(list4)

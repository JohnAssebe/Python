def guest_list(guests):
	for guest in guests:
		guest_name,guest_age,guest_pro=guest
		print("{} is {} years old and works as {}".format(guest_name,guest_age,guest_pro))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

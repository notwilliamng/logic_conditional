def max_101(a,b):
	float (a)
	float (b)
	if a > b:
		return a
	else:
		return b

def max_of_three(a,b,c):
	if a > b and a > c:
		return a
	elif b > a and b>c:
		return b
	else:
		return c

def rental_late_fee(days):
	days = int(days)
	if  days <=0:
		return (0)
	elif days <= 9 and days > 0:
		return (5)
	elif days <=15 and days >9:
		return (7)
	elif days <=24 and days >15:
		return (19)
	else: 
		return (100)


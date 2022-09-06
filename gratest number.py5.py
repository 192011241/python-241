def maximum(a, b, c):

	if (a >= b) and (a >= c):
		largest = a

	elif (b >= a) and (b >= c):
		largest = b
	else:
		largest = c
		
	return largest


# Driven code
a = 70
b = 39
c = 99
print(maximum(a, b, c))

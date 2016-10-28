# Total
def total(numbers):
    sum = 0
    for n in numbers:
    	if type(n) != int:
    		print type(n)
    		return "You must supply only numbers."
    	else:
        	sum += n
    return sum

print total([3, 5, 8, 9, 10, 11, 3, 4, "joe"])

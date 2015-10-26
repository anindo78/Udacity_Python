# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
     if len(list_of_numbers) == 0:
        return 0
    else:
        maximum = list_of_numbers[0]
        if len(list_of_numbers) > 0:
            for i in list_of_numbers:
                maximum = max(maximum, i)
        return maximum
            
            




print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
#More elegant solution
def greatest(list_of_numbers):
	maximum = 0
	for i in list_of_numbers:
		if i > maximum:
			maximum = i
	return maximum
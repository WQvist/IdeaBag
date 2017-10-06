'''
A happy number is defined by the following process: Starting with any 
positive integer, replace the number by the sum of the squares of its 
digits, and repeat the process until the number equals 1 (where it will 
stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers, while 
those that do not end in 1 are unhappy numbers. 
Find the first 8 happy numbers.
'''

numToCheck = 0
numOfHappys = 0
while numOfHappys < 8:	# Find the first 8 happy numbers
	numToCheck += 1
	numString = str(numToCheck)	# Make the number into a string
	summary = 0
	count = 0
	square = 0
	while int(numString) != 1 and count < 5000:	# Assume that no happy number requires more than 5000 loops
		for y in range(len(numString)):
			summary = summary + int(numString[y])**2	# Square the current number and add it to summary
			count+=1
			if y+1 == len(numString):		# If all "chars" in the number have been checked
				numString = str(summary)	# Start checking the new number
				summary = 0
	if int(numString) == 1:
		print(str(numToCheck) + " is a happy number")
		numOfHappys+=1
	

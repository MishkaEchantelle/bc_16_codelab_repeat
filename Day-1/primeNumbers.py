def primeNumbers(num):
	
# '''to return true if the number is a prime number or else return false'''
	
	if (num == 0 or num == 1):
		return False
	elif (num % 2 == 0):
		return False
	else:
		return True
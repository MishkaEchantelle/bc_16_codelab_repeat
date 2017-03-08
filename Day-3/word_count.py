def maxMin():
	 maximum = None
	 minimum =None

	 while True:
	 	input = raw_input("Enter a number:")

	 	if input == "done":
	 		break
	 	if len(input) < 1:
	 		break

	 	try:
	 		number = int(input)
	 	except :
	 		print"Invalid input"
	 		continue

	 	if minimum is None:
	 		minimum = number
	 		maximum = number
	 	elif number < minimum:
	 		minimum = number
	 	elif number > maximum:
	 	    maximum = number

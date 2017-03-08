
def data_type(input_value):
  
	if isinstance(input_value, str):
		return len(input_value)
		
	if input_value == None:
		return "no value"

	if isinstance(input_value, bool):
		return input_value

	if isinstance(input_value, list):
		if len(input_value) == 3:
			return input_value[2]
		else:
			return None

	if isinstance(input_value, int):
		if input_value < 100:
			return "less than 100"
		elif input_value == 100:
			return 'equal to 100'
		else:
			return "more than 100"

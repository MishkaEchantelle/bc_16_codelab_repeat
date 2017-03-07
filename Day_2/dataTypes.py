def data_type(dataType):
  
	if dataType == str:
		return len(dataType)
		
	if dataType == None:
		return "no value"

	if dataType == bool:
		return bool

	if isinstance(dataType, list):
		if len(dataType) == 3:
			return dataType[2]
		else:
			return None

	if type(dataType) == int:
		if data < 100:
			return "less than 100"
		elif data == 100:
			return 'equal to 100'
		else:
			return "more than 100"

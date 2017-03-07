def data_type(dataType):
	if dataType == str:
		return len(dataType)
	if dataType == None:
		return "no value"
	if dataType == bool:
		return dataType
	if dataType == int:
		if dataType < 100 :
			return "less than 100"
		elif dataType > 100
			return "more than 100"
		else
			return "equal to 100"
	if dataType == list:
		if len(dataType) == 3:
			return dataType[2]
		else
			return None



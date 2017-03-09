def find_missing(list_one, list_two):
	if len(list_one) == len(list_two) == 0:
		return 0
	else:
		return set(list_one)-set(list_two)
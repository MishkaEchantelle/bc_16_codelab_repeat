def find_missing_number(list_a, list_b):
	if len(list_a) == len(list_b) == 0:
		return 0
	else:
		return list(set(list_a)-set(list_b))
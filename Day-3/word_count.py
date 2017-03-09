
def words(words_count):
	words_count = {}

	for word in words_count.replace().split():
		if word not in words_count:
			words_count[word] = 1
		else:
			words_count[word] += 1
	for key, val in words_count.items():
		if isinstance(key, str) and key.isdigit():
            words_count[int(key)] = val
            words_count.pop(key)
            
  return words
            

def word_count(wordCount):
	wordCount = {}

	for word in wordCount.read().split():
		if word not in wordCount:
			wordCount[word] = 1
		else:
			wordCount[word] += 1
	for key in wordCount.key():
		print("%s %s " %(key , wordCount[key]))
	word.close():
import re
import csv
import createCSV
import collections

def subWord(a): #Function to strip tags from Tweet

	output = list() #Define List
	
	for word in a:
		
		#RegEx to match any characters within square brackets 
		word = re.sub(r'(\[(.*?)\])', '', word) 

		#Append word to list
		output.append(word)

	return output

def joinmultiWord(words, liststarttags, endtag):

	startFound = 0
	finPhrase = list()
	wordsCopy = list()
	finWord = list()

	for i in range(0, len(words)):

		for tag in liststarttags:

			if tag in words[i] and endtag not in words[i]:

				start = i

				startFound = 1

			elif tag in words[i] and endtag in words[i]:

				finPhrase.append(words[i])

				startFound = 0

		if startFound == 1:

			finWord.append(words[i])

			if endtag in words[i]:

				end = i

				a = words[start:end+1]

				a = (" ".join(a))

				finPhrase.append(a)

				wordsCopy.append(a)

				startFound = 0

				continue

			elif endtag not in words[i]:

				continue

		wordsCopy.append(words[i])

	return wordsCopy

def createTweetLists():

	placeNames = list()
	newStrippedCardList = list()
	newCardList = list()
	endtag = "[#]"
	liststarttags = ["[np]", "[n]", "[c]", "[spp]", "[p]", "[o]", "[pl]", "[cu]", "[t]", "[d]", "[cr]", "[v]"]

	# Tag Key:

	# [np]		= Proper Noun
	# [n]		= Noun
	# [c]		= City
	# [spp] 	= Spatial Preposition Phrase
	# [p]		= Preposition Single
	# [o]		= Organisation
	# [pl]		= Place
	# [cu]		= County
	# [t]		= Town
	# [d]		= District
	# [cr]		= Country
	# [v]		= Village

	with open('.\InputFiles\strippedTweetsString.txt', 'rb') as f:
	    reader = f.readlines()
	    cardList = list(reader)

	for i in range(0, len(cardList)):

		y = str(cardList[i])

		stringList = y.split()

		currentTweet = joinmultiWord(stringList, liststarttags, endtag)

		currentTweetStrip = subWord(currentTweet)

		newStrippedCardList.append(currentTweetStrip)

		newCardList.append(currentTweet)

	return newCardList, newStrippedCardList
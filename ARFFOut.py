import joinStrip
import arff

nonStripped,Stripped = joinStrip.createTweetLists()

def ARFFDataset(list1, list2):

	placeNames = list()
	placenamesLower = list()
	follow = list()
	followAll = list()
	prepositions = list()
	prepPhrase = list()
	searchWords = list()

	with open('.\InputFiles\gazList.txt', 'rb') as f:
		for line in f:
			k = line
			placenamesLower.append(k.strip().lower())

	with open('.\InputFiles\prepositions.txt') as f:
		for line in f:
			k = line
			prepositions.append(k.strip().lower())

	with open('.\InputFiles\searchWords.txt') as f:
		for line in f:
			k = line
			searchWords.append(k.strip().lower())

	for listEle in list1:

		pointer = 0

		for word in listEle:

			wordIndex = listEle[pointer]

			if word.lower() in placenamesLower:

				follow.append('TRUE')

			else:

				follow.append('FALSE')

			if word[0].isupper() and word[0].isalpha():

				follow.append('TRUE')

			else:

				follow.append('FALSE')

			if pointer > 0:

				loc1 = listEle[pointer-1]

				if loc1.lower() in prepositions:

					follow.append('TRUE')

				else:

					follow.append('FALSE')

			else:

				follow.append('FALSE')

			if pointer < (len(listEle)-1):

				loc2 = listEle[pointer+1]

				if loc2.lower() in searchWords:

					follow.append('TRUE')

				else:

					follow.append('FALSE')

			else:

				follow.append('FALSE')

			follow.append("isPlace")

			pointer += 1

			followAll.append(follow)
			follow = list()

	return followAll

def ARFFCreation():

	dataSet = ARFFDataset(Stripped, nonStripped)

	attList = [
	('Gazetteer', ['TRUE', 'FALSE']),
	('CapitalLetter', ['TRUE', 'FALSE']),
	('Preposition', ['TRUE', 'FALSE']),
	('FollowingWord', ['TRUE', 'FALSE']),
	('Place', ['yes', 'no'])
	]

	obj = {
		'description': u'',
		'relation': 'PlaceNames',
		'attributes': attList,
		'data': dataSet,
	}

	with open('.\CreatedCSVs\TestData.arff', 'a') as f:
		f.write(arff.dumps(obj))
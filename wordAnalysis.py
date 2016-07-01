import csv
import re
import createCSV
import joinStrip

foundNames = list()
placenamesLower = list()
preListBefore = list()
preListAfter = list()
preDict = {}
unDictAfter = {}
unDictBefore = {}

with open('.\InputFiles\prepositions.txt') as f:
	for line in f:
		k = line
		preDict[k.strip()] = 0

with open('.\InputFiles\gazList.txt', 'rb') as f:
	for line in f:
		k = line
		placenamesLower.append(k.strip().lower())

nonStripped,Stripped = joinStrip.createTweetLists()

for listEle in Stripped:

	pointer = 0

	for word in listEle:

		if word.lower() in placenamesLower:
		
			if pointer > 0:

				loc1 = listEle[pointer-1]
				preListBefore.append(loc1.lower())	

			if pointer < (len(listEle)-1):

				loc2 = listEle[pointer+1]
				preListAfter.append(loc2.lower())

		pointer += 1

createCSV.createAfter(preListAfter, preDict, unDictAfter)
createCSV.createBefore(preListBefore, preDict, unDictBefore)
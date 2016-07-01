import csv

def createAfter(list1, dict1, dict2):

	for i in range(0, len(list1)):

		if list1[i] in dict1: #Check if key exists in Dict1
			dict1[list1[i]] += 1 #If so, increment value

		elif list1[i] in dict2: #Check if key exists in Dict2
			dict2[list1[i]] += 1

		else:
			dict2[list1[i]] = 1 #If key does not exist in Dict 1 or Dict 2, add new key

	#Write Dicts to CSV

	with open('.\CreatedCSVs\preListAfter.csv', 'wb') as f:
		w = csv.DictWriter(f, dict1.keys())
		w.writeheader()
		w.writerow(dict1)

	with open('.\CreatedCSVs\unDictAfter.csv', 'wb') as f:
		w = csv.DictWriter(f, dict2.keys())
		w.writeheader()
		w.writerow(dict2)

def createBefore(list1, dict1, dict2):

	for i in range(0, len(list1)):

		if list1[i] in dict1: #Check if key exists in Dict1
			dict1[list1[i]] += 1 #If so, increment value

		elif list1[i] in dict2: #Check if key exists in Dict2
			dict2[list1[i]] += 1

		else:
			dict2[list1[i]] = 1 #If key does not exist in Dict 1 or Dict 2, add new key

	#Write Dicts to CSV

	with open('.\CreatedCSVs\preListBefore.csv', 'wb') as f:
		w = csv.DictWriter(f, dict1.keys())
		w.writeheader()
		w.writerow(dict1)

	with open('.\CreatedCSVs\unDictBefore.csv', 'wb') as f:
		w = csv.DictWriter(f, dict2.keys())
		w.writeheader()
		w.writerow(dict2)

#The following are a sety of functions used to produce various text documents

def createFile(list1):

	with open('.\CreatedCSVs\markedText.txt', 'a') as f:
		f.writelines(str(list1)+'\n')

def createStrippedFileList(twitterList):

	with open('.\CreatedCSVs\strippedTweetsList.txt', 'a') as f:
		f.writelines(str(twitterList)+'\n')

def createStrippedFile(twitterString):

	with open('.\CreatedCSVs\strippedTweetsString.txt', 'a') as f:
		f.writelines(twitterString+'\n')

def createStrippedGaz(gazList):

	with open('.\InputFiles\gazList.txt', 'a') as f:
		f.writelines(gazList+'\n')
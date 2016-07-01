import createCSV
import csv
import re

def taggingPrep():

	# Open file as f
	with open('.\InputFiles\cardifffull.csv', 'rb') as f:
	    reader = csv.reader(f)
	    # Create list 'cardList' from file
	    cardList = list(reader)

	for i in range(0, len(cardList)):

		# Convert current index to string
		y = str(cardList[i])

		# Regular Expression to replace all special characters except-
		# Alphanumeric and Whitespace with a blank entry ''
		subString = re.sub('[^a-zA-Z\d\s]', '', y)

		#Join stipped string to remove multiple whitepaces
		subString = ' '.join(subString.split())

		#Call function to create text file of stripped Tweets 
		createCSV.createStrippedFile(subString)

#Execute function
taggingPrep()
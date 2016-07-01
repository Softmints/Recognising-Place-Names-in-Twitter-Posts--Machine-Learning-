import createCSV
import csv
import re

def gazPrep():

	# Open file as f
	with open('.\InputFiles\gazList.csv', 'rb') as f:
	    reader = csv.reader(f)
	    # Create list 'cardList' from file
	    gazList = list(reader)

	for i in range(0, len(gazList)):

		# Convert current index to string
		y = str(gazList[i])

		# Regular Expression to replace all special characters except-
		# Alphanumeric and Whitespace with a blank entry ''
		subString = re.sub('[^a-zA-Z\d\s]', '', y)

		#Join stipped string to remove multiple whitepaces
		subString = ' '.join(subString.split())

		#Call function to create text file of stripped Tweets 
		createCSV.createStrippedGaz(subString)

#Execute function
gazPrep()
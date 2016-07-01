import nltk 
import csv
import createCSV

def tagText(fname):

	with open('C:\Users\Softmints\Desktop\Diss\Code\InputFiles\%s.csv' %fname, 'rb') as f:
		reader = csv.reader(f)

		for row in reader:

			text = nltk.word_tokenize(str(row).strip('[' ']'))
			Temp = nltk.pos_tag(text)
			createCSV.createFile(Temp)

tagText("cardiff500")
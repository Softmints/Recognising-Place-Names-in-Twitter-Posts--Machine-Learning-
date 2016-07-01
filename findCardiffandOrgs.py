import csv
import re

string = "Cardiff"

with open('C:\Users\Softmints\Desktop\Diss\Code\InputFiles\Cardiff500.csv', 'rb') as f:
    reader = csv.reader(f)
    cardList = list(reader)

    for i in range(0, len(cardList)):

		y = str(cardList[i])

		y = re.sub('[^a-zA-Z\d\s:]', '', y)

		x = y.split()

		for j in range(0, len(x)):

			if string.lower() in x[j]:

				temp = x[j]
				print temp
			
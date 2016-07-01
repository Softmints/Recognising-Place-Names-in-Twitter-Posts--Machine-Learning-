import MySQLdb as mdb
import csv
import re
import createCSV

# Open database connection
db = mdb.connect("localhost","root","","gazetteer" )

# prepare a cursor object
cursor = db.cursor()

# SQL query construction
sql = "SELECT FULL_NAME_ND FROM gazetteer_ppl"

try:
   # Execute command
   cursor.execute(sql)

   rows = cursor.fetchall()

   # Open a .csv file
   fp = open('.\InputFiles\gazList.csv', 'w')

   # Write database rows to .csv file
   myFile = csv.writer(fp)
   myFile.writerows(rows)

   fp.close()

# Error handling
except:
   print "Error: unable to fetch data"

# disconnect from server
db.close()
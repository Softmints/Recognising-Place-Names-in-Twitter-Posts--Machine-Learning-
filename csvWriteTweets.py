import MySQLdb as mdb
import csv

# Open database connection
db = mdb.connect("localhost","root","","miner" )

# prepare a cursor object
cursor = db.cursor()

# SQL query construction
sql = "SELECT text FROM tweets_cardiff"

try:
   # Execute command
   cursor.execute(sql)

   rows = cursor.fetchall()

   # Open a .csv file
   fp = open('cardifffull.csv', 'w')

   # Write database rows to .csv file
   myFile = csv.writer(fp)
   myFile.writerows(rows)

   fp.close()

# Error handling
except:
   print "Error: unable to fetch data"

# disconnect from server
db.close()
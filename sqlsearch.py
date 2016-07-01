import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","","miner" )

# Set cursor  object
cursor = db.cursor()

# Set SQL query for specified table and fields
sql = "SELECT text FROM tweets_cardiff \
		WHERE text LIKE '%cardiff%'"

try:
   # Execute command
   cursor.execute(sql)
   # Fetch all the rows and create a list of lists
   results = cursor.fetchall()
   for row in results:
      text = row[0]
      print "text=%s" % \
             (text)
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
from databaseinterface import DatabaseInterface

dbi = DatabaseInterface.get_shared_instance()

#
'''
values = [ (6,"Deshpande"),(7,"Nikhil Jain") , (8,"Krishnan"), (9,"Ishan"), (10,"Banerjee") ]
for val in values:
	dbi.execute( "INSERT INTO test (id,name) VALUES (%s,%s)",val )
#'''

selected = dbi.execute("SELECT * FROM test",None)

#print selected.fetchall()
cursor=dbi.execute("INSERT INTO TEST (id,name) VALUES (%s,%s)", (69,"Nikhil Iyer") )
print cursor.lastrowid
#print selected.fetchall()

exit(0)

from socialscoreupdater import SocialScoreUpdater as SSU

ssu = SSU()
ssu._load_feed_statistics()

print ssu._feed_statistics
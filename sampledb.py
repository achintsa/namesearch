import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="rs1234",
                  db="namelist")
x = conn.cursor()



with open("firstnames.out") as f:
    fnames = f.read().splitlines()

with open("lastnames.out") as g:
    lnames = g.read().splitlines()


#fullnames=[]

for i in fnames:
	for j in lnames:

		try:
		   x.execute("""INSERT INTO User VALUES (%s,%s,%s)""",("",i,j))
		   conn.commit()
		except:
			print "failed query"
			conn.rollback()


conn.close()

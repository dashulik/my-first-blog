import MySQLdb

db = MySQLdb.connect('localhost','root','popovadasha3473','dasha')

cur = db.cursor();
cur.execute('SELECT * FROM USERS')

db.close()
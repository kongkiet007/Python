'''import sqlite3 #import sqlite3
conn = sqlite3.connect("E:\Kongkiet_Python\example.db")
c = conn.cursor() #create a cursor object 
'''#c.execute ('''CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,
   #fnme varchar(30) NOT NULL,
   #IName varchar(30) NOT NULL,
   #email varchar(100) NOT NULL)''')'''
#c.execute('''INSERT INTO users (id,fnme,IName,email) VALUES (NULL,"A","A","A") ''')
#c.execute('''INSERT INTO users VALUES (NULL,"B","B","B") ''')
#conn.commit() #save (commit) the change
#conn.close() #close the connecton when done'''''''''

#import sqlite3
#def insertTousers (fnme,IName,email) :
 #   try :
#        conn = sqlite3.connect('E:\Kongkiet_Python\example.db')
 #       c = conn.cursor()
#
 #       sql = ''' INSERT INTO users (fnme,IName,email) VALUES (?,?,?) '''
  #      data = (fnme,IName,email)
   #     c.execute(sql,data)
    #    conn.commit ()
     #   c.close ()
#
 #   except sqlite3.Error as e:
  #      print('Failed to insert : ',e)
   # finally :
    #    if conn :
     #       conn.close ()
#
#insertTousers('Kongkiet','Pitugpon','kong.r5r5007@gmail.com')
#insertTousers('Kong','Kiet','007')

import sqlite3

conn = sqlite3.connect(r"E:\Kongkiet_Python\example.db")
c= conn.cursor()

try :
    c.execute(' SELECT * FROM users ORDER BY ID  ')
    conn.commit ()
    result = c.fetchall()
    for x in result :
        print (x)
    c.close()

except sqlite3.Error as e:
    print(e)

finally :
    if conn :
         conn.close ()    
    
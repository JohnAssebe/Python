'''
created at 11:37 PM 10/9/2019
@author:Yohannes Assebe(John)
Basics on Database connection
'''
import mysql.connector as mysql
from DBconfig import mysqlconfig
from pprint import pprint
conn=mysql.connect(**mysqlconfig.mysqlconfig)
cursor=conn.cursor()
#firstpythonDb="firstpythonDb"
##try:
##    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(firstpythonDb))
##except mysql.Error as err:
##    print("There {}".format(err))
#===========we should use a database first in order to know where to works======= 
#cursor.execute("USE firstpythonDb")

#===========This command works to show the list of tables that are found in the database==============
#cursor.execute("SHOW TABLES")
#===============create table in a database with primary key============
##cursor.execute("CREATE TABLE BOOK( \
##         Book_ID INT NOT NULL AUTO_INCREMENT, \
##         Book_Title VARCHAR(30) NOT NULL,   \
##         Book_Page INT NOT NULL,   \
##         PRIMARY KEY (Book_ID)   \
##        )ENGINE=InnoDB")


#================creating table in mysql DB with foreign key to make a connection for these two tables==============

##cursor.execute("CREATE TABLE Quotations( \
##         Quote_ID INT, \
##         Quatation VARCHAR(300),   \
##         Books_Book_ID INT ,   \
##         FOREIGN KEY (Books_BOOK_ID)   \
##         REFERENCES BOOK(Book_ID)    \
##         ON DELETE CASCADE  \
##        )ENGINE=InnoDB")
cursor.execute("use firstpythondb")
cursor.execute("SHOW COLUMNS FROM QUOTATIONS")
pprint(cursor.fetchall())
conn.close()

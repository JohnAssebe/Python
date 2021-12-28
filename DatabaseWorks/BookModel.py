'''created at 10:07 AM 10/10/2019
    @author:Yohannes Assebe(John)
 '''
 
from DBconfig import mysqlconfig
import mysql.connector as mysql
class Model:
    def __init__(self):
        self.conn,self.cursor=self.connect()
    def connect(self):
        conn=mysql.connect(**mysqlconfig.mysqlconfig)
        cursor=conn.cursor()
        return conn,cursor
    def close(self):
        self.cursor.close()
        self.conn.close()
    def createDB(self,DBName):
        self.cursor.execute("CREATE DATABASE {}".format(DBName))
    def useDB(self,DBName):
        self.cursor.execute("USE {}".format(DBName))
    def insertBook(self,booktitle,page,bookQuote):
        self.cursor.execute("INSERT INTO book(Book_Title,Book_Page) VALUES ((%s),(%s))",(booktitle,page))
        self.cursor.execute("INSERT INTO quotations(Quote_ID,Quatation) VALUES((%s),(%s))",(page,bookQuote))
        self.conn.commit()
    def showBooks(self,title):
        self.cursor.execute("SELECT * FROM book WHERE Book_Title=\"{}\"".format(title))
        return self.cursor.fetchall()
    def showQuote(self,page):
        self.cursor.execute("SELECT Quatation FROM quotations Where Quote_ID={}".format(page))
        return self.cursor.fetchall()
    def updateBooks(self,title,page):
        self.cursor.execute("UPDATE book SET Book_Page=(%s) WHERE Book_Title=(%s)",(page,title))
        self.conn.commit()
    def updateQuote(self,page,bookQuote):
        self.cursor.execute("UPDATE quotations SET Quatation=(%s) WHERE Quote_ID=(%s)",(bookQuote,page))
        self.conn.commit()
    def deleteBook(self,title):
        self.conn,self.cursor=self.connect()
        return self.cursor.execute("DELETE FROM book where Book_Title=(%s)",(title))

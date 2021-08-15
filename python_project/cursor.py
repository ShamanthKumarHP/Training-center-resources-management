#pointer connection to DB
import mysql.connector as db
Username = input("Database user name: ")
Username = 'root'
PW = input("Database Password: ")
PW = '6666'
Host = input("Host: ")
Host = 'localhost'
Database = input("Database name: ")
Database = 'computerparadise'

cnx = db.connect(user='{0}'.format(Username),
                     password='{0}'.format(PW),
                     host='{0}'.format(Host),
                     database='{0}'.format(Database),
                     charset='utf8')

ptr=cnx.cursor()


          
          
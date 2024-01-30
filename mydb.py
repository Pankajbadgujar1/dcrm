import mysql.connector

dataBase = mysql.connector.connect(
    HOST = 'localhost',
    USER = 'root',
    PASSWORD ='123456'
)

#prepare a cursor object
cousorObject = dataBase.cursor()

#create a database

#cousorObject.execute("CREATE DATABASE eld")

#print("All done!")
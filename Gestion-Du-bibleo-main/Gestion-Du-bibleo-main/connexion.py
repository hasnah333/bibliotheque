import mysql.connector

class connexion:
   
      

    	
    def connectionWithmysql(self):
      mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="gestionetudetlivre")
      return mydb
    

    
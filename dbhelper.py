import databases
import mysql.connector
import sys

from questionary import password

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="hit-db-demo")
            self.mycursor = self.conn.cursor()
        except:
            print("Some error occured. Could not connect to the database")
            sys.exit(0)
        else:
            print("Connected to Database")

    def register(self, name, email, password):
        try:
            self.mycursor.execute(f"""
            INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{name}', '{email}', '{password}');
            """)
            self.conn.commit()
        except:
            return -1
        else:
            return 1


    def search(self, email, password):
        self.mycursor.execute(f"""
        SELECT * FROM users WHERE email LIKE '{email}' AND password LIKE '{password}'
        """)

        data = self.mycursor.fetchall()

        # print(data)
        return data

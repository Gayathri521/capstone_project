import mysql.connector
class DatabaseConnection():

    def connect(self,localhost,username,password,database,port):
        self.hostname=localhost
        self.username=username
        self.password=password
        self.database=database
        self.portnum=port

        self.connect=mysql.connector.connect(host=self.hostname,username=self.username,password=self.password,database=self.database,port=self.portnum)
        self.cur = self.connect.cursor()

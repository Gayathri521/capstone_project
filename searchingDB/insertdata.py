import mysql.connector
from searchingDB.DBConnection  import DatabaseConnection
from capstoneExceptions.MysqlExceptions import MysqlError
class InsertinDB(DatabaseConnection):
    def __init__(self):
        self.conn = self.connect("localhost","root","Gayathri1234@","myhcl",3306)
    def insert(self,files):
        self.files=files
        self.insertcur=self.connect.cursor()
        for f in self.files:
            sql="insert into fileinfo(filename) values(%s);"
            self.insertcur.execute(sql,(f,))
            self.connect.commit()
        print("files added successfully")
# try:
#     f=["hema","siri"]
#     obj=InsertinDB()
#     print(obj)
# except mysql.connector.Error as err:
#     raise MysqlError(f'{err.msg}',err.errno)
#
#
#
#
#
#



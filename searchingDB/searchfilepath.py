import mysql.connector
from searchingDB.DBConnection import DatabaseConnection
from capstoneExceptions.MysqlExceptions import MysqlError
class searchFile(DatabaseConnection):
    def search(self,filename):
        print("searching in database")
        self.filename=filename
        sql="""select * from fileinfo where filename like'%{0}'""".format(filename)
        self.cur.execute(sql)
        data=self.cur.fetchall()
        return data

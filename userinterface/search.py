import logging
logging.basicConfig(filename='..//Logger//capstone.log', level=logging.DEBUG, format=('%(asctime)s-%(name)s-%(levelname)s-%(message)s'))
from SearchfilesinDrives.Searchfiles import searchfilesdrives
from searchingDB.DBConnection import DatabaseConnection
from searchingDB.searchfilepath import searchFile
from capstoneExceptions.MysqlExceptions import MysqlError
from searchingDB.insertdata import InsertinDB
import mysql.connector
import time
import openpyxl as xl
def userdata():
    dir=input("Enter the drive like c:// d:// \n")
    filename=input("Enter the filename with extension like demo.txt\n")
    logging.info(f"Drive name{dir} file name{filename}")
    dbobj=searchFile()
    logging.info(f"class used{searchFile.__name__}")
    wb=xl.load_workbook("C://testdata//Testfiles.xlsx")
    ws=wb.active
    try:
        dbobj.connect("localhost","root","Gayathri1234@","myhcl",3306)
        logging.info("myhcl database is connected")
        result=dbobj.search(filename)
    except mysql.connector.Error as err:
        logging.exception(err, exc_info=True)
        raise MysqlError(f'{err.msg}',err.errno)
    finally:
       pass

    if len(result)==0:
        print("Not found in database")
        print("Now searching in Drives...")
        logging.info("Not found in Database")
        logging.info("Now searching in Drives")
        start_time=time.time()
        obj=searchfilesdrives()
        logging.info(f'for searching in drive {searchfilesdrives.__name__} is used')
        files=obj.searchfiles(dir,filename)
        ws.cell(rows=1,column=1).value=str(files)
        wb.save("C://testdata//Testfiles.xlsx")
        wb.close()
        inserobj=InsertinDB()
        inserobj.insert(files)
        logging.info(f'files found {files}')
        print(files)
        obj.start()
        end_time=time.time()
        logging.info(f'time taken{end_time - start_time}')
        logging.info("Ending")
        print(end_time-start_time)
    else:
        print("Found in database")
        print(result)
userdata()
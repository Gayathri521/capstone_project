import os
import openpyxl as xl
class searchdrives():
    """
    this module helps to find all drives present in pc
    67 to 91 for  ascii value
    chr() to convert ascii value to char
    """
    def __init__(self):
        self.drives=[]
        self.workbook=xl.load_workbook("c://testdata//Testdrives.xlsx")
    def searchmydrives(self)->list:
        for i in range(67,91):
            if os.path.exists(chr(i)+":"):
                self.drives.append(chr(i))
        return self.drives
dr=searchdrives()
data=str(dr.searchmydrives())
print(data)
sheet=dr.workbook.active
sheet.cell(row=1,column=1).value=data
dr.workbook.save("C://testdata//Testdrives.xlsx")
dr.workbook.close()
# dr.searchmydrives()
# print(dr.drives)


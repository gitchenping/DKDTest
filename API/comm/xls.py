# -*- coding:utf-8 -*-
import xlrd

class readExcel(object):
    def __init__(self, path):
        self.path = path

    @property
    def getSheet(self):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheet_by_index(0)

        return sheet



    def getRows(self):
        # 获取行数
        rows = self.getSheet.nrows
        return rows


    def getCols(self):
        # 获取列数
        cols = self.getSheet.ncols
        return cols

    # 以下是分别获取每一列的数值
    # row_data = sheet.row_values(0)     # 获得第1行的数据列表
    def getName(self, column_index):
        if column_index <= self.getCols:
            ColumnName = []
            for i in range(1, self.getRows()):
                ColumnName.append(self.getSheet.cell_value(i, column_index))
            return ColumnName
        else:
            print("输入的column不合法！")

    def getcase(self,apilist=None):
        sheet=self.getSheet
        rows = self.getRows()
        caselist=[]
        print rows

        if not apilist:
            i=1
            while i <rows:
                siglecase=self.getSheet.row_values(i)
                caselist.append(siglecase)
                i+=1
            # print "is"+ str(caselist)
        else:
            print apilist
            for apiname in apilist:
                i=1
                while i < rows:
                    # 读取case_name的那一行

                     if sheet.row_values(i)[1] == apiname:
                         siglecase = self.getSheet.row_values(i)
                         # print siglecase
                         for col in range(3, 8):
                             siglecase[col] = siglecase[col].replace('\n', '')

                         caselist.append(siglecase)
                     i += 1
        return caselist



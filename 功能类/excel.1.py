import xlrd
import xlwt
from datetime import datetime
import time

def read(file, sheet_index=1):
    """

    :param file: 文件路径
    :param sheet_index: 读取的工作表索引
    :return: 二维数组
    """
    workbook = xlrd.open_workbook(file)
    # all_sheets_list = workbook.sheet_names()
    # print("本文件中所有的工作表名称:", all_sheets_list)
    # 按索引读取工作表
    sheet = workbook.sheet_by_index(sheet_index)
    print("工作表名称:", sheet.name)
    print("行数:", sheet.nrows)
    print("列数:", sheet.ncols)

    # 按工作表名称读取数据
    # second_sheet = workbook.sheet_by_name("b")
    # print("Second sheet Rows:", second_sheet.nrows)
    # print("Second sheet Cols:", second_sheet.ncols)
    # 获取单元格的数据
    # cell_value = sheet.cell(1, 0).value
    # print("获取第2行第1列的单元格数据:", cell_value)
    
    data = []
    lists = []
    for i in range(0, sheet.nrows):
        for j in range(0,len(sheet.row_values(i))):
            if sheet.row_values(i)[j]=="韦美鹏":
                # strname = "\t\t" + sheet.row_values(0)[j-1] + "\t\t" + sheet.row_values(i)[j-1]+"\t\t\t\t"+sheet.row_values(i)[j]
                if type(sheet.row_values(i)[0])==type('str'):
                    lists.append(xlrd.xldate.xldate_as_datetime(sheet.row_values(i-1)[0],0).strftime('%Y-%m-%d'))
                    lists.append(sheet.row_values(i-1)[1] + "下午")
                    lists.append(sheet.row_values(0)[j-1])
                    lists.append(sheet.row_values(i)[j-1])
                    lists.append(sheet.row_values(i)[j])
                    #print(xlrd.xldate.xldate_as_datetime(sheet.row_values(i-1)[0],0).strftime('%Y-%m-%d') + sheet.row_values(i-1)[1] + "下午" + strname)
                    data.append(lists)
                    lists=[]
                else:
                    lists.append(xlrd.xldate.xldate_as_datetime(sheet.row_values(i)[0],0).strftime('%Y-%m-%d'))
                    lists.append(sheet.row_values(i)[1] + "上午")
                    lists.append(sheet.row_values(0)[j-1])
                    lists.append(sheet.row_values(i)[j-1])
                    lists.append(sheet.row_values(i)[j])
                    #print(xlrd.xldate.xldate_as_datetime(sheet.row_values(i)[0],0).strftime('%Y-%m-%d') + sheet.row_values(i)[1] + "上午" + strname)
        #data.append(sheet.row_values(i))
                    data.append(lists)
                    lists=[]
    return data


def save(data,path):

    file = xlwt.Workbook(encoding='utf-8')
    table = file.add_sheet('data')

    for i,p in enumerate(data):
        for j,q in enumerate(p):
            
            table.write(i,j,q)

    file.save(path)
    return "操作完成"

if __name__ == '__main__':
    
    data = read(r"C:\Users\tyl\Desktop\zhiliang.xlsx")
    print(save(data,r"C:\Users\tyl\Desktop\工具\demo.xlsx"))
    
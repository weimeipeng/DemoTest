#-*- coding:utf-8 -*-

__author__ = "苦叶子"


import csv

if __name__ == "__main__":
    print("python csv文件写读操作示例")

    # 写csv文件
    print("写入一些简单数据到csv_data.csv文件中")
    with open('csv_data.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile,  # csvfile为打开要写的文件对象
            delimiter=',' # 分隔符
            )
        spamwriter.writerow(['csv_demo'] * 5 + ['DeepTest'])
        spamwriter.writerow(['hello', 'Study Python3', 'Auto Testing'])

        csvfile.close()

    print("读取csv_data.csv问内容")
    with open('csv_data.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print("row的类型： ", type(row))
            print(row)

            # 遍历每行中每个数据项
            for data in row:
                print(data, "  ")
        
        f.close()
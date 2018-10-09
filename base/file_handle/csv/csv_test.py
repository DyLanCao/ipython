# -- coding: utf-8 --

import csv
 
#读取csv文件方式1
csvFile = open("csvData.csv", "r")
reader = csv.reader(csvFile)  # 返回的是迭代类型
data = []
for item in reader:
    print(item)
    data.append(item)
              
print(data)
csvFile.close()


#读取csv文件方式2
with open("csvData.csv", "r") as csvfile:
    reader2 = csv.reader(csvfile)
    for item2 in reader2:
        print(item2)
csvFile.close()

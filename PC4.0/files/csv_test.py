import csv


# 读取本地 csv 文件
date = csv.reader(open ('info.csv', 'r'))
# 循环捡出每一行信息
for user in date:
    print(user)

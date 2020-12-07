# -*- coding = utf-8 -*-
# @Time : 2020/12/6 15:29
# @Author : QQQ
# @File : textXlwt.py
# @Software : PyCharm


import xlwt

''' xlwt 的使用演示'''
# workbook = xlwt.Workbook(encoding='utf-8')  # 创建 Workbook 对象
# worksheet = workbook.add_sheet('sheet1')  # 创建工作表sheet
# worksheet.write(0, 0, 'hello')  # 写入数据，第一个参数'行'，第二个参数'列'，第三个参数内容
# workbook.save('student.xls')  # 保存数据表格

'''写入一个九九乘法表'''
# workbook = xlwt.Workbook(encoding='utf-8')
# worksheet = workbook.add_sheet('sheet1')
# for i in range(0, 9):  # range左闭右开[1,10)
#     for j in range(0, i+1):
#         worksheet.write(i, j, '%d * %d = %d' % (i+1, j+1, (i+1)*(j+1)))
#
# workbook.save('student.xls')

text = '''
hello
world
'''
print('多行字符串输出')
print(text)



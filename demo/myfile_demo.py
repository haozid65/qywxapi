# -*- coding: utf-8 -*-
# Time: 2022/4/28 12:07
# Author: Gavin
import os

Base_path = os.getcwd()
MyFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in MyFiles:
#     print(os.getcwd() +'\demo'+ filename)
# print(Base_path)

file = open('bai.txt', encoding='utf-8')
print(file.readlines())

read_file = open('bai.txt', 'w+', encoding='utf-8')
read_file.write('Hello World')
print(read_file.readlines())
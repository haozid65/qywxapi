# -*- coding: utf-8 -*-
# Time: 2022/3/30 20:34
# Author: Gavin


# def add(x, *y):
#     for num in y:
#         x += num
#     return x
#
# print(add(1,2,3,4))

# def personinfo(name, age, **message):
#     print(f'name:{name}, age:{age},{message}')
# personinfo('张三', 22, message={'city':'Shanghai', 'area':'Pudong'})

def User(self, first_name, last_name, city, area):
    self.first_name = first_name
    self.last_name = last_name
    self.city = city
    self.area = area

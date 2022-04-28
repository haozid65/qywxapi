# -*- coding: utf-8 -*-
# Time: 2022/4/27 11:43
# Author: Gavin
import os
import yaml

class GetYamlData:
    def __init__(self, file):
        if os.path.exists(file):
            self.file = file
        else:
            print('Yaml文件不存在！！！')

    @property   # 设置属性，调用data方法时可通过调用属性，不需要带括号
    def get_data(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        return data


if __name__ == '__main__':
    res = GetYamlData('test_data.yaml').get_data
    print(res)
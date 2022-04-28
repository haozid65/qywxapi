# -*- coding: utf-8 -*-
# Time: 2022/4/27 10:27
# Author: Gavin
import yaml
import os


class GetYaml:
    def __init__(self, file_path):
        # 判断文件是否存在
        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            print('没有找到{}文件路径'.format(file_path))

    def read_yaml(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            r = file.read()
        return r

    def get_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            r = file.read()
        result = yaml.load(r, yaml.FullLoader)

        if result[0]['pwd'] == None:
            print('没有找到密码')
        else:
            return result[0]['pwd']



if __name__ == '__main__':
    print(GetYaml('test_data.yaml').get_data())
# -*- coding: utf-8 -*-
# Time: 2022/4/27 9:57
# Author: Gavin
import yaml
import os

yaml_path = os.path.abspath(os.path.dirname(os.getcwd()))+"/config/configdata.yaml"
with open(yaml_path, 'r', encoding='utf-8') as file:
    f_res = file.read()
d = yaml.load(f_res, Loader=yaml.FullLoader)
print(d, type(d))
print('---------------------------------')
print(d['weixin']['corpid'])


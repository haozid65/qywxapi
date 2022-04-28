# -*- coding: utf-8 -*-
# Time: 2022/4/27 10:24
# Author: Gavin
import yaml


yaml_path = 'test_data.yaml'
with open(yaml_path, 'r', encoding='utf-8') as file:
    data = file.read()
d = yaml.load(data, Loader=yaml.FullLoader)
print(d)
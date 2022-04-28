# -*- coding: utf-8 -*-
# Time: 2022/4/26 18:23
# Author: Gavin

import yaml
import os


filepath = os.path.join(os.path.dirname(__file__), 'configdata.yaml')
with open(filepath, 'r', encoding='utf-8') as file:
    configdata = yaml.load(file, yaml.FullLoader)
    print(configdata)
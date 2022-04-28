# -*- coding: utf-8 -*-
# Time: 2022/4/28 9:50
# Author: Gavin

stuff = {"rope": 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def Inventory(inventory):
    print('Inventory: ')
    total = 0
    for k, v in inventory.items():
        total += v
        print(v, k)
    print('Total number of items: ' + str(total))


Inventory(stuff)
# -*- coding: utf-8 -*-
# Time: 2022/4/28 9:10
# Author: Gavin

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apples pies': 1, 'apples': 15}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('P92 Number of things being brought: ')
print('- Apples ' + str(totalBrought(allGuests, 'apples')))
print('- Cups ' + str(totalBrought(allGuests, 'cups')))
print('- Cakes ' + str(totalBrought(allGuests, 'cakes')))
print('- Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print('- Apple Pies ' + str(totalBrought(allGuests, 'apples pies')))
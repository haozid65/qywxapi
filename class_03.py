# -*- coding: utf-8 -*-
# Time: 2022/3/30 21:42
# Author: Gavin
# 继承


class RobotOne:     # 第一代机器人
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def walking_on_ground(self):
        print(self.name + '只能在平地上走，有障碍物就会摔倒')

    def robot_info(self):
        print("{0}年生产的机器人{1},是中国研发的".format(self.year, self.name))


class RobotTwo:     # 第二代机器人继承于第一代机器人的类
    def __init__(self, year, name):
        self.year = year
        self.name = name
    def walking_on_ground(self):
        print(self.name + '可以在平地上平稳的行走')

    def walking_avoid_block(self):
        print(self.name + '可以避开障碍物')

# 第二代机器人实例
# 继承的类 是否要用到初始化 请看是否从父类里面继承了
# t = RobotTwo(1929, "Gaga")
# t.walking_avoid_block()


class RobotThree(RobotTwo, RobotOne):     # 第三代机器人继承于第一代和第二代机器人的类
    def jump(self):
        print(self.name + "可以单膝跳跃")
r3 = RobotThree("2000","大王")
r3.walking_on_ground()
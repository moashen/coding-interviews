# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        Flag = False
        for index in range(len(array)):
            if target in array[index]:
                Flag = True
        return Flag

# 题目描述
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# 运行时间：240ms
# 占用内存：3156k

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        list1 = []
        list2 = []
        for n in array:
            if n%2 == 1:
                list1.append(n)
            else:
                list2.append(n)
        return list1+list2
        
# 题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
# 运行时间：10ms
# 占用内存：3156k
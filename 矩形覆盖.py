# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, n):
        if n == 0:
            return 0
        a = 1
        b = 1
        for i in range(n):
            a,b = b,a+b
        return a
        
# 题目描述
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# 运行时间：20ms
# 占用内存：3156k
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        a = 1
        b = 1
        for i in range(number):
            a,b = b,a+b
        return a
        
# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 运行时间：20ms
# 占用内存：3156k
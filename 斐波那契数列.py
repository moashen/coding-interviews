# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        a = 0
        b = 1
        for i in range(n):
            a,b = b,a+b
        return a
        
# 题目描述
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
# n<=39
# 运行时间：20ms
# 占用内存：3156k
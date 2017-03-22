# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        return sum([(n>>i & 1) for i in range(0,32)])

# 题目描述
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 运行时间：30ms
# 占用内存：3156k
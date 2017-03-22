# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        L = []
        while head!=None:
            L.append(head)
            head=head.next
        if k>len(L) or k<1:
            return
        return L[-k]

# 题目描述
# 输入一个链表，输出该链表中倒数第k个结点。
# 运行时间：20ms
# 占用内存：3148k
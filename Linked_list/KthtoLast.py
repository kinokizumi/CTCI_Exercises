#!/usr/bin/python3

###################
#
# This script returns from kth to the last elem of a LL
#
###################

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertLL(self, arr):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            for item in arr:
                curr.next = Node(item)
                curr = curr.next
        else:
            return "no head assigned"
    
    def printLL(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

###################

## Solution 1: use two pointers => O(N) time, O(1) space

def GetKtoLast(head, k):
    p1 = head
    p2 = head
    for i in range(k):
        p1 = p1.next
        if p1 is None:
            return "k out of bound"
    while p1.next:
        p1 = p1.next
        p2 = p2.next
    return p2

## Solution 2: recursion => O(N) time, O(N) space

#class Index:
#    def __init__(self):
#        self.val = -1
#
#def GetKtoLast(head, k):
#    idx = Index()
#    return Helper(head, k, idx)
#
#def Helper(head, k, idx):
#    if head is None:
#        return None
#    node = Helper(head.next, k, idx)
#    idx.val = idx.val + 1
#    if idx.val == k:
#        return head
#    return node

###################

LL = LinkedList()
LL.head = Node(3)
LL.insertLL([6,9,5,2,7,8,1,4])
KthVal = GetKtoLast(LL.head, 3)
print(KthVal.val)

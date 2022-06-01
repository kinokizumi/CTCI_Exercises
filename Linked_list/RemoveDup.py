#!/usr/bin/python3

###################
#
# This script removes duplicates from unsorted linked list
#
###################

## Solution n.1 => O(N) time, O(N) space

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertLL(self, data):
        newNode = Node(data)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode

def LLtoArr(LL_in):
    arr = []
    curr = LL_in.head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr

def RemoveDup(LL_in):
    record = {}
    curr = LL_in.head
    prev = curr
    while curr:
        if curr.val in record:
            prev.next = curr.next
        else:
            record[curr.val] = 1
            prev = curr
        curr = curr.next
    return LL_in

###################

LL = LinkedList()
LL.insertLL(4)
LL.insertLL(3)
LL.insertLL(5)
LL.insertLL(4)
LL.insertLL(3)
LL.insertLL(7)
LL.insertLL(5)
print(LLtoArr(LL))
RemoveDup(LL)
print(LLtoArr(LL))
        

#!/usr/bin/python3

###################
#
# This script deletes a node in a singly linked list while the head is not given
#
###################

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def InsertLL(self, arr):
        if not self.head:
            self.head = Node(arr[0])
            arr = arr[1:]
        curr = self.head    
        while curr.next:
            curr = curr.next
        for elem in arr:
            curr.next = Node(elem)
            curr = curr.next

    def PrintLL(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

    def GetNode(self, data):
        curr = self.head
        while curr:
            if curr.val == data:
                return curr
            curr = curr.next
        return None

###################

def DeleteMiddle(node):
    next_n = node.next
    node.val = next_n.val
    node.next = next_n.next    

###################

arr = ["a", "b", "c", "d", "e", "f"]
LL = LinkedList()
LL.InsertLL(arr)
node = LL.GetNode("c")

print(LL.PrintLL())

DeleteMiddle(node)
print(LL.PrintLL())

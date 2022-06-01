#!/usr/bin/python3

############################
#
# This scripts look for path between two nodes in directed graph
#
############################

from collections import deque

############################

class Node:
    def __init__(self, data):
        self.val = data
        self.visited = 0
    def __hash__(self):
        return hash(self.val)
    def __eq__(self, other):
        return hash(self) == hash(other)

class Graph:
    def __init__(self):
        self.nodes = {}

    def addEdge(self, data1, data2):
        node1 = Node(data1)
        node2 = Node(data2)
        if node1 not in self.nodes:
            self.nodes[node1] = [node2]
        else:
            if node2 not in self.nodes[node1]:
                self.nodes[node1].append(node2)

    def findRoute(self, data1, data2):
        node1 = Node(data1)
        node2 = Node(data2)
        if node1 == node2:
            return True
        visitedNode = deque([node1])
        copy = self
        while len(visitedNode) > 0:
            curr = visitedNode.popleft()
            if copy.nodes.get(curr):
                #import pdb; pdb.set_trace()
                for node in copy.nodes.get(curr):
                    if node.visited == 0:
                        if node == node2:
                            return True
                        else:
                            visitedNode.append(node)
                            node.visited = 1
            else:
                continue
            copy.nodes.pop(curr)
        return False

############################

graph = Graph()
graph.addEdge('s', 'a')
graph.addEdge('s', 'c')
graph.addEdge('a', 'e')
graph.addEdge('c', 'a')
graph.addEdge('e', 'c')
graph.addEdge('d', 'a')

print(graph.findRoute('s', 'e'))

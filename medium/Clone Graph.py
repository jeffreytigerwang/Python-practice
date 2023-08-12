# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] # public List<Node> neighbors;
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # if not node:
        #     return node
        #
        # nodeMap = {}
        # q = [node]
        #
        # for n in q:
        #     nodeMap[n] = Node(n.val)
        #
        #     for neighbor in n.neighbors:
        #         if neighbor and neighbor not in q:
        #             q.append(neighbor)
        #
        # for n in q:
        #     if n.neighbors:
        #         for neighbor in n.neighbors:
        #             nodeMap[n].neighbors.append(nodeMap[neighbor])
        #
        #
        # return nodeMap[node]

        if not node:
            return node

        nodeMap = {}

        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]

            nodeMap[node] = Node(node.val)

            for neighbor in node.neighbors:
                nodeMap[node].neighbors.append(dfs(neighbor))

            return nodeMap[node]

        return dfs(node)









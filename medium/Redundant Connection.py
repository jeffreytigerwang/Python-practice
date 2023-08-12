# https://leetcode.com/problems/redundant-connection/description/
from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # graphMap = defaultdict(list)
        # ans = []
        # def dfs(x, y):
        #     if x in path:
        #         return False
        #
        #     if x == y:
        #         return True
        #
        #     for node in graphMap[x]:
        #         if dfs(node, y):    # we know x is connected to y and node is connected to x; thus if node is connected to y, we have a cycle.
        #             return True
        #
        #
        # for x, y in edges:
        #     path = set()
        #
        #     if dfs(x, y):
        #         ans = [x, y]
        #
        #     graphMap[x].append(y)
        #     graphMap[y].append(x)
        #
        # return ans

        # findUnion
        par = [i for i in range(len(edges) + 1)]  # +1 because node is labeled from 1 to n
        rank = [1] * (len(edges) + 1)

        def find(node):
            parent = par[node]

            while parent != par[parent]:
                # par[parent] = par[par[parent]]  # Optimize time complexity; do not need to loop again when we search next time
                parent = par[parent]

            return parent

        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)

            if p1 == p2:
                return True

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return False

        for x, y in edges:
            if union(x, y):
                return [x, y]

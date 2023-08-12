# https://leetcode.com/problems/lru-cache/

# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#
#         self.next = None
#         self.prev = None
#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}
#
#         self.left = Node(0, 0)
#         self.right = Node(0, 0)
#
#         self.left.next = self.right
#         self.right.prev = self.left
#
#     def insert(self, node):
#         nodeBeforeRight = self.right.prev
#         right = self.right
#
#         node.next = right
#         node.prev = nodeBeforeRight
#
#         right.prev = node
#         nodeBeforeRight.next = node
#
#     def remove(self, node):
#         prev = node.prev
#         next = node.next
#
#         prev.next = node.next
#         next.prev = node.prev
#
#     def get(self, key: int) -> int:
#         if key in self.cache.keys():
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#
#             return self.cache[key].val
#
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache.keys():
#             self.remove(self.cache[key])
#
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])
#
#         if len(self.cache) > self.capacity:
#             LRU = self.left.next
#             self.remove(LRU)
#             del self.cache[LRU.key]

# ordered dict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            res = self.cache.pop(key)
            self.cache[key] = res

            return res

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache.pop(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


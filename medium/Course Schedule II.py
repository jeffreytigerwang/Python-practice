# https://leetcode.com/problems/course-schedule-ii/
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cycle = set()
        courseDict = {}
        res = []

        for course, pre in prerequisites:
            if course not in courseDict.keys():
                courseDict[course] = []

            courseDict[course].append(pre)

        # Courses without prerequisites will not show up in dict. Need to append them first.
        for course in range(numCourses):
            if course not in courseDict.keys():
                res.append(course)

        def dfs(course):
            # Checking for loop
            if course in cycle:
                return False

            if course not in courseDict.keys():
                return True

            cycle.add(course)

            for c in courseDict[course]:
                if not dfs(c):
                    return False

            res.append(course)
            # Avoid loop
            cycle.remove(course)

            # Reduce time complexity
            del courseDict[course]

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res

        # cycle = set()
        # path = set()
        # courseDict = {c: [] for c in range(numCourses)}
        # res = []
        #
        # for course, pre in prerequisites:
        #     courseDict[course].append(pre)
        #
        # def dfs(course):
        #     if course in cycle:
        #         return False
        #
        #     if course in path:
        #         return True
        #
        #     cycle.add(course)
        #
        #     for curr in courseDict[course]:
        #         if not dfs(curr):
        #             return False
        #
        #     res.append(course)
        #     cycle.remove(course)
        #     path.add(course)
        #
        #     return True
        #
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return []
        #
        # return res
        #

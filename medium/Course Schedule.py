# https://leetcode.com/problems/course-schedule/
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        courseDict = {}

        for course, pre in prerequisites:
            if course not in courseDict.keys():
                courseDict[course] = []

            courseDict[course].append(pre)

        def dfs(course):
            # Checking for loop
            if course in path:
                return False

            if course not in courseDict.keys():
                return True

            path.add(course)

            for c in courseDict[course]:
                if not dfs(c):
                    return False

            # Avoid loop
            path.remove(course)

            # Reduce time complexity
            del courseDict[course]

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
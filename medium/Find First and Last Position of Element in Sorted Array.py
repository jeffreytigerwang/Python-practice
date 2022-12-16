class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def findLeftIndex(tempNums, tempTarget):
            length = len(tempNums)
            left = 0
            right = length - 1
            resL = -1

            while left <= right:
                temp = ((right - left) // 2) + left
                # print(temp)

                if tempNums[temp] == tempTarget:
                    resL = temp

                if tempNums[temp] < tempTarget:
                    left = temp + 1
                else:
                    # if tempNums[temp] > tempTarget:
                    right = temp - 1

            return resL

        def findRightIndex(tempNums, tempTarget):
            length = len(tempNums)
            left = 0
            right = length - 1
            resR = -1

            while left <= right:
                temp = ((right - left) // 2) + left
                # print(temp)

                if tempNums[temp] == tempTarget:
                    resR = temp

                if tempNums[temp] <= tempTarget:
                    left = temp + 1
                else:
                    # if tempNums[temp] > tempTarget:
                    right = temp - 1

            return resR

        left = findLeftIndex(nums, target)
        right = findRightIndex(nums, target)
        ans = [left, right]
        return ans



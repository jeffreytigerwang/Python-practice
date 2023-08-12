from typing import List


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        red, white, blue = 0, 0, 0

        for n in nums:
            if n == 0:
                red += 1

            elif n == 1:
                white += 1

            else:
                blue += 1

        nums[0: red] = 0
        nums[red: white] = 1
        nums[white:] = 2

class Solution2(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        new_dict = {new_list: [] for new_list in range(3)}
        res = []

        for i in nums:
            if i in new_dict:
                new_dict[i].append(i)

        for value in new_dict.values():
            for i in value:
                res.append(i)

        for i in range(len(nums)):
            nums[i] = res[i]


class Solutio2:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        high = len(nums) - 1
        mid = 0

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1



def main():
    nums = [2,0,2,1,1,0]

    test = Solution()
    test.sortColors(nums)

if __name__ == "__main__":
    main()
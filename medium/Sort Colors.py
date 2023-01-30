class Solution(object):
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

        print(nums)

def main():
    nums = [2,0,2,1,1,0]

    test = Solution()
    test.sortColors(nums)

if __name__ == "__main__":
    main()
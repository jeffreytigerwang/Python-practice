class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        # fill nums1 with leftover numbers in nums2

        if n > 0:
            nums1[: n] = nums2[: n]


t1 = [1, 2, 3, 0, 0, 0]
n1 = 3
t2 = [2, 5, 6]
n2 = 3

test1 = Solution()
print(test1.merge(t1, n1, t2, n2))

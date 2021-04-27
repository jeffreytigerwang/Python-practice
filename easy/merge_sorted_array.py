class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index1 = len(nums1) - 1
        i1 = m-1
        i2 = n-1

        while i2>=0:
            if nums1[i1] > nums2[i2] and i1 >= 0:
                nums1[index1] = nums1[i1]
                i1 = i1-1
            else:
                nums1[index1] = nums2[i2]
                i2 = i2-1
            index1 = index1-1


        print(nums1)


t1 = [1, 2, 3, 0, 0, 0]
n1 = 3
t2 = [2, 5, 6]
n2 = 3

test1 = Solution()
print(test1.merge(t1, n1, t2, n2))

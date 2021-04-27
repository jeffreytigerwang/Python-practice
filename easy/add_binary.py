badd = {'000': ['0', '0'],
        '001': ['1', '0'],
        '010': ['1', '0'],
        '011': ['0', '1'],
        '100': ['1', '0'],
        '101': ['0', '1'],
        '110': ['0', '1'],
        '111': ['1', '1']}


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = '0'
        s1 = len(a)
        s2 = len(b)

        if s1 > s2:
            b = '0' * (s1 - s2) + b
            s2 = s1
        elif s1 < s2:
            a = '0' * (s2 - s1) + a
            s1 = s2

        sum = [''] * s1


        # while (s1-1 >= 0 or s2-1 >= 0):

        for i in range(s1 - 1, -1, -1):
            temp = a[i] + b[i] + c
            sum[i], c = badd[temp]

        sum = (c + ''.join(sum)) if c == '1' else (''.join(sum))
        return sum


a = '11'
b = '1'

answer = Solution()
print(answer.addBinary(a, b))

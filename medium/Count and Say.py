# https://leetcode.com/problems/count-and-say/description/

class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'

        res = '11'

        for i in range(n - 2):
            count = 1
            tempSay = ''
            # temp = res[0]

            for j in range(1, len(res)):
                if res[j] == res[j - 1]:
                    count += 1

                    # if j == len(res) - 1:
                    #     tempSay += str(count) + res[j]
                        # print(tempSay)

                else:
                    tempSay += str(count) + res[j - 1]

                    count = 1

                if j == len(res) - 1:
                    tempSay += str(count) + res[j]



            res = tempSay
            print(res)

        # print(res)
        return res

sol = Solution()

n = 4

sol.countAndSay(n)

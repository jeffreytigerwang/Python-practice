class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        stringToChar = list(s)

        for i in range(len(stringToChar)):
            if stringToChar[i] == 'I':
                if i < (len(stringToChar) - 1) and stringToChar[i+1] == 'V':
                    result += 4
                elif i < (len(stringToChar) - 1) and stringToChar[i+1] == 'X':
                    result += 9
                else:
                    result += 1
            elif stringToChar[i] == 'V':
                if i > 0 and stringToChar[i-1] == 'I':
                    continue
                else:
                    result += 5
            elif stringToChar[i] == 'X':
                if i < (len(stringToChar) - 1) and stringToChar[i+1] == 'L':
                    result += 40
                elif i < (len(stringToChar) - 1) and stringToChar[i+1] == 'C':
                    result += 90
                elif i > 0 and stringToChar[i-1] == 'I':
                    continue
                else:
                    result += 10
            elif stringToChar[i] == 'L':
                if i > 0 and stringToChar[i-1] == 'X':
                    continue
                else:
                    result += 50
            elif stringToChar[i] == 'C':
                if i > 0 and stringToChar[i-1] == 'X':
                    continue
                elif i < (len(stringToChar) - 1) and stringToChar[i+1] == 'D':
                    result += 400
                elif i < (len(stringToChar) - 1) and stringToChar[i + 1] == 'M':
                    result += 900
                else:
                    result += 100
            elif stringToChar[i] == 'D':
                if i > 0 and stringToChar[i-1] == 'C':
                    continue
                else:
                    result += 500
            elif stringToChar[i] == 'M':
                if i > 0 and stringToChar[i-1] == 'C':
                    continue
                else:
                    result += 1000
        return result

string = 'MCMXCIV'
test = Solution()
print(test.romanToInt(string))


class Solution:
    def isValid_0(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        right = [')', ']', '}']

        temp = []

        for letter in s:
            if letter in left:
                temp.append(letter)
            elif letter in right:
                if len(temp) <= 0:
                    return False
                elif right.index(letter) != left.index(temp.pop()):
                    return False
        return not temp

    def isValid(self, s):
        p_map = {'{': '}', '[': ']', '(': ')'}
        valid_input = ['{', '[', '(']
        temp = []
        for i in s:
            if i in valid_input:
                temp.append(i)
            elif temp and i == p_map[temp[-1]]:
                temp.pop()
            else:
                return False
        print(temp)
        return not temp

s = "()[]"
test1 = Solution()
print(test1.isValid(s))

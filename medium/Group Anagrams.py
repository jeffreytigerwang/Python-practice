class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        dictionary = {}

        for string in strs:
            tempStr = "".join(sorted(string))
            if tempStr not in dictionary:
                dictionary[tempStr] = []
                dictionary[tempStr].append(string)
            else:
                dictionary[tempStr].append(string)

        for value in dictionary.values():
            res.append(value)

        # print(dictionary.values())
        # print(res)
        return res

def main():
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs = ["a"]

    ans = Solution()
    ans.groupAnagrams(strs)

if __name__ == "__main__":
    main()
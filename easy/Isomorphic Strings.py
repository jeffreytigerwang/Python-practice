class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        for c1, c2 in zip(s, t):
            if (c1 in sDict.keys() and sDict[c1] != c2) or (c2 in tDict.keys() and tDict[c2] != c1):
                return False

            sDict[c1] = c2
            tDict[c2] = c1

        return True
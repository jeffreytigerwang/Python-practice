# https://leetcode.com/problems/push-dominoes/
import collections


# My solution - slow
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)

        while True:
            temp = dominoes.copy()

            for i in range(len(temp)):
                if temp[i] == 'L':
                    if i > 0 and temp[i - 1] == '.':
                        if i > 1 and temp[i - 2] == 'R':
                            continue
                        else:
                            dominoes[i - 1] = 'L'
                elif temp[i] == 'R':
                    if i < len(temp) - 1 and temp[i + 1] == '.':
                        if i < len(temp) - 2 and temp[i + 2] == 'L':
                            continue
                        else:
                            dominoes[i + 1] = 'R'

            if temp == dominoes:
                return ''.join(dominoes)


class Solution1:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        q = collections.deque()
        for i, d in enumerate(dom):
            if d != '.':
                q.append((i, d))

        while q:
            i, d = q.popleft()

            if d == 'L':
                if i > 0 and dom[i - 1] == '.':
                    # Does not need to check for i - 2 because it will be handled in line 51
                    q.append((i - 1, 'L'))
                    dom[i - 1] = 'L'

            elif d == 'R':
                if i + 1 < len(dom) and dom[i + 1] == '.':
                    if i + 2 < len(dom) and dom[i + 2] == 'L':
                        q.popleft() # We know next element in q is L and it will balance current R --> skip it
                    else:
                        q.append((i + 1, 'R'))
                        dom[i + 1] = 'R'

        return ''.join(dom)


sol = Solution()
dominoes = ".L.R...LR..L.."
print(sol.pushDominoes(dominoes))
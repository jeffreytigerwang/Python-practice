# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(root, word):
            curr = root

            for i, c in enumerate(word):
                if c == '.':
                    for child in curr.children.values():
                        if dfs(child, word[i + 1:]):    # dfs(child, word[1:]) is wrong because c will update during the for loop,
                            return True                 # whereas word remained the same.
                    return False
                else:
                    if c not in curr.children:
                        return False

                    curr = curr.children[c]

            return curr.end

        return dfs(self.root, word)













# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
'''
https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
'''
#%%
class WordDictionary:
    def __init__(self):
        # TODO: do i even need to point end of word
        self.root = [False, {}]

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur[1]:
                cur[1][c] = [False, {}]
            cur = cur[1][c]
        
        cur[0] = True

    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(node, pos):
            c = word[pos]
            
            if c==".":
                for i in node[1]:
                    if dfs(node[1][i], pos+1): return True
                
                return False
            else:
                if c not in node[1]:
                    return False
                
                if pos == n-1: return node[1][c][0]
                return dfs(node[1][c], pos+1)

        return dfs(self.root, 0)

s = WordDictionary()
# %%
s.addWord("apple")
# %%
s.search("ap..e")
# %%

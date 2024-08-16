'''
https://leetcode.com/problems/implement-trie-prefix-tree/description/
'''
#%%
class Trie_node:
    def __init__(self):
        self.child = {}
        self.end =  False

class Trie:
    def __init__(self):
        self.root = [False, {}]# parent: list[bool, {child_tree}]

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur[1]:
                cur[1][c] = [False, {}]# default value
            cur = cur[1][c]
        
        cur[0] = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur[1]:
                return False
            cur = cur[1][c]
        
        return cur[0]

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur[1]:
                return False
            cur = cur[1][c]
        
        return True

s = Trie()
# %%
s.insert("apple")
#%%
s.insert("app")
s.search("app")
# %%

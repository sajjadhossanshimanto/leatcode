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
        self.root = Trie_node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = Trie_node()
            cur = cur.child[c]
        
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        
        return True

s = Trie()
# %%
s.insert("apple")
s.insert("app")
s.search("app")
# %%

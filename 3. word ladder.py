'''
https://leetcode.com/problems/word-ladder/description/
'''
#%%
from typing import List
from collections import defaultdict, deque


inf = float("inf")
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:# not in list
            return 0
        
        def linkable(w1, w2):
            c=0
            for i in range(len(beginWord)):
                if w1[i]!=w2[i]:
                    c+=1
                    if c>1: return False
            
            return True

        # create graph
        adj = defaultdict(list)
        wordList.append(beginWord)
        wordList = list(set(wordList))
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                w1 = wordList[i]
                w2 = wordList[j]
                if linkable(w1, w2):
                    adj[w1].append(w2)
                    adj[w2].append(w1)
        
        visit = set()
        ans = inf
        q = deque([(0, beginWord)])
        while q:
            dis, node = q.popleft()
            
            for child in adj[node]:
                if child==endWord:
                    ans = min(ans, dis+1)
                elif child in visit: continue
                else:
                    visit.add(child)
                    q.append((dis+1, child))

        return 0 if ans==inf else ans

g = Solution()
#%%
# ans = 5
g.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
# %%
# ans = 0
g.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"])
# %% wa2
# ans = 2
g.ladderLength("a", "c", ["a", "b", "c"])
# %%

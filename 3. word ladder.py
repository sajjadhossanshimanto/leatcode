'''
https://leetcode.com/problems/word-ladder/description/
'''
#%%
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:# not in list
            return 0
        end = wordList.index(endWord)
        
        for i in range(end-1, -1, -1):# should i return 1 if end and start firrer by one
            word = wordList[i]
            c = 0
            for j in range(len(beginWord)):
                if beginWord[j]!=word[j]:
                    c+=1
            
            if c==1:
                print(end, i)
                return end-i+1# 1 for the 1st conversion from start word to word on list

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

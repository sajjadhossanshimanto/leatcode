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
                return end-i

g = Solution()
#%%
g.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
# %%
g.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"])
# %%

# https://leetcode.com/problems/word-break/description/

#%%
from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def dfs(start=0)-> bool:
            if start==len(s): return True

            for i in wordDict:
                if s[start:start+len(i)]==i:
                    if dfs(start+len(i)): return True
            
            return False
        
        return dfs()

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if s[i: i+len(word)]==word:
                    dp[i] = dp[i+len(word)]
                    
                    if dp[i]: break
        
        return dp[0]


s= Solution()
# %%
# ans: true
# out: false
s.wordBreak(
    "cars", ["car","ca","rs"]
)
# %%
s.wordBreak(
    s = "leetcode", wordDict = ["leet","code"]
)
# %%
s.wordBreak(
    s = "applepenapple", wordDict = ["apple","pen"]
)
# %%

# https://leetcode.com/problems/word-break/description/

#%%
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(start=""):
            if start==s: return True
            if len(start)>=len(s): return False

            for i in wordDict:
                if dfs(start+i): return True
            
            return False
        
        return dfs()

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

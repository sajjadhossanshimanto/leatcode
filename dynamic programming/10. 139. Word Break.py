# https://leetcode.com/problems/word-break/description/

#%%
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for i in wordDict:
            s = s.replace(i, "")
        
        return not s

s= Solution()
# %%
# ans: true
# out: false
s.wordBreak(
    "cars", ["car","ca","rs"]
)
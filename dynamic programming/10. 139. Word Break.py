# https://leetcode.com/problems/word-break/description/

#%%
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        combi = set([""])
        for i in wordDict:
            for j in combi.copy():
                new = j+i
                combi.add(new)
                if new==s: return True
        
        return combi

s= Solution()
# %%
# ans: true
# out: false
s.wordBreak(
    "cars", ["car","ca","rs"]
)
# %%

# https://leetcode.com/problems/decode-ways/description/

#%%
from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:

        @lru_cache
        def dfs(start):
            if start==len(s):
                return 1
            if s[start]=="0": return 0
            
            # take one
            r=dfs(start+1)

            # take 2
            if start<len(s)-1:
                if s[start: start+2] <= "26":
                    r+=dfs(start+2)
            
            return r
            
        return dfs(0)

# %%
s = Solution()
# ans: 3
s.numDecodings("226")
# %%
# ans: 2
s.numDecodings("12")
# %%
# ans = 0
# out = 2
s.numDecodings("06")
# %% tl
s.numDecodings("111111111111111111111111111111111111111111111")
# %%

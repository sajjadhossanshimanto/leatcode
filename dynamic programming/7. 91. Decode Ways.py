# https://leetcode.com/problems/decode-ways/description/

#%%
from itertools import permutations


class Solution:
    def numDecodings(self, s: str) -> int:
        count = [0]
        def dfs(start):
            if start==len(s):
                count[0]+=1
                return 
            
            # take one
            dfs(start+1)

            # take 2
            if start<len(s)-1:
                if s[start: start+2] <= "26":
                    dfs(start+2)
            
        dfs(0)
        return count[0]

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
# %%

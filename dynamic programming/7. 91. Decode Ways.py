# https://leetcode.com/problems/decode-ways/description/

#%%
from itertools import permutations


class Solution:
    def numDecodings(self, s: str) -> int:
        return len(s)*(len(s)-1)
        count = len(set(s))
        ways = set()
        for i in range(len(s)-1):
            ways.add(s[i]+s[i+1])
        
        return count*len(ways)

# %%
s = Solution()
s.numDecodings("226")
# %%

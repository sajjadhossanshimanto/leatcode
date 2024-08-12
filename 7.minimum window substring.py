'''
https://leetcode.com/problems/minimum-window-substring/
'''
#%%
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pattern = defaultdict(lambda :0)
        mismatch = defaultdict(lambda :0)
        for i in t:
            pattern[i]+=1
            mismatch[i]+=1

        ans = (0, len(s)-1)# l, r
        l, r = 0,  0
        while r < len(s):
            if not mismatch:
                # if matched
                if (r-l+1) < ans[1]-ans[0]+1:
                    ans = (l, r)
                
                while not mismatch:
                    if s[l] in pattern:
                        mismatch[s[l]]+=1
                        if mismatch[s[l]] > pattern[s[l]]:
                            mismatch[s[l]] -= 1
                    l+=1

            if s[r] in mismatch:
                mismatch[s[r]] -= 1
                if mismatch[s[r]]==0:
                    mismatch.pop(s[r])
            r+=1
                
        return s[ans[0]:ans[1]+1]


s = Solution()
# %%
# "BANC"
s.minWindow(s = "ADOBECODEBANC", t = "ABC")
# %%

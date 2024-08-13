'''
https://leetcode.com/problems/minimum-window-substring/
'''
#%%
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s): return ""

        pattern = defaultdict(lambda :0)
        mismatch = defaultdict(lambda :0)
        for i in t:
            pattern[i]+=1
            mismatch[i]+=1

        ans = (0, len(s)-1)# l, r
        window = defaultdict(lambda :0)
        l = 0
        for r in range(len(s)):
            char = s[r]
            if char in pattern:
                window[char] += 1
                
                if s[r] in mismatch:
                    mismatch[s[r]] -= 1
                    if mismatch[s[r]]==0:
                        mismatch.pop(s[r])

            while not mismatch:
                if (r-l+1) < (ans[1]-ans[0]+1):
                    ans = (l, r)

                char = s[l]
                if char in pattern:
                    window[char] -= 1
                    if window[char] < pattern[char]:
                        mismatch[char] += 1
                l+=1

        return s[ans[0]:ans[1]+1]


s = Solution()
# %%
# "BANC"
s.minWindow(s = "ADOBECODEBANC", t = "ABC")
# %%
# "a"
s.minWindow(s = "a", t = "a")
# %%
# ""
s.minWindow(s= "a", t="aa")
# %%

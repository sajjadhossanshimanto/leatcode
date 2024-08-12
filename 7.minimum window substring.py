'''
https://leetcode.com/problems/minimum-window-substring/
'''
#%%
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(lambda :0)
        pattern = defaultdict(lambda :0)
        for r in range(len(t)):
            pattern[t[r]]+=1
            window[s[r]]+=1
        l, r = 0,  len(t)-1

        def match():
            for i in pattern:
                if i not in window: return False
                if pattern[i] > window[i]: return False
            
            return True

        while r<=len(s):
            if match(): break

            r+=1
            window[s[r]]+=1

        while 1:
            s[l]
                
        return s[:r+1]


# %%

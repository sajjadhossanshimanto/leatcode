'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
'''
#%%
from typing import List


inf = float('inf')
class Solution:
    def removeDuplicates(self, s: str, k: int) -> int:
        i = 0
        while len(s)>=k and i!=len(s)-1:
            char = s[i]
            for j in range(i+1, i+k):# forward checking
                # as `i+k` is unsecuire
                if j<len(s) and s[j]!=char:
                    i = j
                    break

            if j-i+1==k:# if not breaked. +1 for including both end-point
                s = "".join([s[:i], s[j+1:]])
                # back steping
                while i-1>=0 and s[i]==s[i-1]:
                    i-=1

        return s

s = Solution()
# %%
# ans = "abcd"
s.removeDuplicates(s = "abcd", k = 2)
# %%
# ans = "aa"
s.removeDuplicates(s = "deeedbbcccbdaa", k = 3)
# %%
# ans = "ps"
s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2)
# %%

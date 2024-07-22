#TODO: check I'th question
#%%
from typing import List


inf = float('inf')
class Solution:
    def removeDuplicates(self, s: str, k: int) -> int:
        i = 0
        while len(s)>=k and i!=len(s)-1:
            char = s[i]
            for j in range(i+1, i+k):
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
s.removeDuplicates("deeedbbcccbdaa", k=3)
# %%

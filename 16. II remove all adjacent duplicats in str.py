#TODO: check I'th question
#%%
from typing import List


inf = float('inf')
class Solution:
    def removeDuplicates(self, s: str, k: int) -> int:
        i = k-1# zero index
        while i!=len(s):
            char = s[i]
            for j in range(i-1, i-k, -1):
                if s[j]!=char:
                    i +=1
                    break
            else:# if not breaked
                s = "".join([s[:i-k+1], s[i+1:]])
                # back steping
                # while 
            # return
        return s

s = Solution()
# %%
s.removeDuplicates("deeedbbcccbdaa", k=3)
# %%

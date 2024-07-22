#%%
from typing import List
from itertools import combinations


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = set()
        for i in arr:
            temp = ans.union(set(i))
            if len(temp)==len(ans)+len(i):
                ans = temp
        
        return len(ans)

s = Solution()
# %%
s.maxLength(["un", "iq", "ue"])
# %%

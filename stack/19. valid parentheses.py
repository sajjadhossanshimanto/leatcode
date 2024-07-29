#%%
from typing import List
from pathlib import Path


inf = float('inf')
class Solution:
    def isValid(self, s: str) -> bool:
        close_pair = {
            ")":"(",
            "}":"{",
            "[":"["
        }
        opened = []
        for i in s:
            if i in close_pair:
                if opened.pop() != close_pair[i]:
                    return False
            else:
                opened.append(i)
        
        return True

s= Solution()
# %%
# 1
s.isValid("()")
# %%
# ans = 1
# out = 0
s.isValid(r"()[]{}")
# %%
# ans = 0
s.isValid("(]")
# %%

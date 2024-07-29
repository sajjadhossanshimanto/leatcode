'''
https://leetcode.com/problems/valid-parentheses/description/
'''
#%%
class Solution:
    def isValid(self, s: str) -> bool:
        close_pair = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        opened = []
        for i in s:
            if i in close_pair:
                if not opened:# safety for pop
                    return False
                if opened.pop() != close_pair[i]:
                    return False
            else:
                opened.append(i)
         
        if opened: return False
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

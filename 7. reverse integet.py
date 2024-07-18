'''
https://leetcode.com/problems/reverse-integer/description/
'''
#%%
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            return -int(str(-x)[::-1])
        return int(str(x)[::-1])

#%%
n=-120
Solution().reverse(n)
# %%

'''
https://leetcode.com/problems/reverse-integer/description/
'''
#%%
class Solution:
    def reverse(self, x: int) -> int:
        if 2147483647<x or x<-2147483647:
            return 0
        
        if x<0:
            return -int(str(-x)[::-1])
        return int(str(x)[::-1])

#%%
n=-120
# %% wa1036
# ex = 0
n = 1534236469
Solution().reverse(n)

# %%

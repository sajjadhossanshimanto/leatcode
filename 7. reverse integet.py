'''
https://leetcode.com/problems/reverse-integer/description/
'''
#%%
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x = -int(str(-x)[::-1])
        else:
            x = int(str(x)[::-1])
        
        if 2147483647<x or x<-2147483647:
            return 0
        return x

#%%
n=-120
# %% wa1036
# ex = 0
n = 1534236469
Solution().reverse(n)

# %%

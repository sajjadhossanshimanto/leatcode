#%%
# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 1]
        if n==1: return arr[-1]
        
        for i in range(2, n+1):
            arr.append(arr[-1]+arr[-2])
        
        return arr[-1]

#%%
s = Solution()
s.climbStairs(2)
# %%

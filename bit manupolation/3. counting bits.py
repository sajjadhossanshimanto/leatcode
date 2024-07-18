'''
https://leetcode.com/problems/counting-bits/
'''
#%%
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [0]+[format(i, "b").count("1") for i in range(1, n+1)]

#%%
n = 5
[0]+[format(i, "b").count("1") for i in range(1, n+1)]
# %%
# don't know how it works
# if even right shifted number
# if odd right shifted + 1
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
                
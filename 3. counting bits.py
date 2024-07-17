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

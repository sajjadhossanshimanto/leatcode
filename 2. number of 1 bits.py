'''
https://leetcode.com/problems/number-of-1-bits/description/
'''
#%%
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

#%%
n=128
bin(n).count("1")

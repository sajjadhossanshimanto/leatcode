'''
https://leetcode.com/problems/reverse-bits
'''
#%%
from itertools import islice

class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n, "b")[::-1]
        n = "".join([n, "0"*(32-len(n))])
        return int(n, 2)


#%%
n = 43261596
Solution().reverseBits(n)
# %%

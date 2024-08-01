'''
https://leetcode.com/problems/remove-k-digits/
'''
#%%
from typing import List
from itertools import islice


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num): return "0"

        n = len(num) - k
        stack = []
        for i in num:
            while stack and i>stack[-1]: 
                # build stack prefering smaller number
                stack.pop()
                
            stack.append(i)

        #TODO: what if removal reduces stack ln tobe less than `n`
        res = ''.join(islice(stack, len(stack)-n, None))
        return res or "0"

s = Solution()
# %%
s.removeKdigits('1432219', k=3)
# %%
s.removeKdigits("10200", k=1)
# %%
s.removeKdigits("10", 2)
# %%

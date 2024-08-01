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
        ans = 0
        stack = []
        for i in num:
            while stack and i<stack[-1] and k>0:# we can at max remove k. any more removal would rest error
                # build stack prefering smaller number
                stack.pop()
                k-=1
            stack.append(i)

        ans = ''.join(
            islice(stack, len(stack)-k) if k else stack
        ).lstrip("0")

        return ans or "0"

s = Solution()
# %%
s.removeKdigits('1432219', k=3)
# %%
s.removeKdigits("10200", k=1)
# %%
s.removeKdigits("10", 2)
#%%
s.removeKdigits("112", 1)
# %%

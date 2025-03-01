# https://leetcode.com/problems/happy-number/description/
# leetcode easy


#%%
def breakdown_number(n):
    while n!=0:
        n, digit = divmod(n, 10)
        yield digit

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while 1:
            if n == 1: return True
            if n in seen: return False# cycle ditected
            seen.add(n)

            new = 0
            for digit in breakdown_number(n):
                new += digit*digit
            n = new

s = Solution()
# %%
s.isHappy(68)
# %%

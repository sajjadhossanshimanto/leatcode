# see web
#%%
from typing import List
from itertools import accumulate


def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

def mul(a, b):
    return a*b

def dev(a, b):
    return a/b

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+": plus,
            "-": minus,
            "*": mul,
            "/": dev
        }
        stack = []
        for i in tokens:
            if i in op:
                for j in accumulate(stack, op[i]):
                    pass
                stack = [j]

            else:
                stack.append(int(i))
        
        return stack[-1]# TODO: can there be more than one
        # return j

s = Solution()
#%%
s.evalRPN(['2', "1", "+", "3", "*"])
# %%

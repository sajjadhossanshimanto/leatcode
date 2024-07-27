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
                b = stack.pop()
                a = stack.pop()
                j = op[i](a, b)
                stack.append(j)

            else:
                stack.append(int(i))
        
        return stack[-1]# TODO: can there be more than one
        # return j

s = Solution()
#%%
# ans = 9
s.evalRPN(['2', "1", "+", "3", "*"])
# %%
# ans = 6
s.evalRPN(["4","13","5","/","+"])
# %%
# ans = 22
s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
# %%

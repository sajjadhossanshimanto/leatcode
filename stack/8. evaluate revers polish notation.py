'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
'''
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
    # rount it toward zero
    return int(a/b)

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
                stack.append(op[i](a, b))

            else:
                stack.append(int(i))
        
        return stack[-1]

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

'''
https://leetcode.com/problems/min-stack/description/
'''
#%%
from typing import List


inf = float('inf')
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(
            min(val, self.min_stack[-1]) if self.min_stack else val
        )

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.stack:
            return self.min_stack[-1]
# %%
a = MinStack()
a.push(46)
a.push(46)
a.push(47)
a.pop()
print(a.getMin())
a.pop()
print(a.getMin())
a.pop()
a.push(47)
print(a.getMin())
a.push(-48)
print(a.getMin())
a.pop()
print(a.getMin())
# %%

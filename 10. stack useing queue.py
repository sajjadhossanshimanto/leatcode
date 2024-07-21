#%%
from typing import List
from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        q = deque()
        while q:
            ele = self.q.pop()
            q.appendleft(ele)
        self.q = q
        
        return ele

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        # return len(self.q) == 0
        return not bool(self.q)
'''
https://leetcode.com/problems/maximum-frequency-stack/description/
'''
#%%
from heapq import heappop, heappush


class FreqStack:
    def __init__(self):
        self.feq = {}
        self.prio = []# of (feq, pos)

    def push(self, val: int) -> None:
        # self.stack.append(val)# do  need that
        self.feq[val] = self.feq.get(val, 0)# default dict
        self.feq[val]+=1
        
        heappush(self.prio, (-self.feq[val], val))

    def pop(self) -> int:
        while 1:
            feq, val = heappop(self.prio)
            if self.feq[val]==-feq:
                self.feq[val]-=1
                if self.feq[val]==0:
                    del self.feq[val]
                else:
                    heappush(self.prio, (-self.feq[val], val))
                return val


obj = FreqStack()
# %%
l = [5, 7, 5, 7, 4, 5]
for i in l:
    obj.push(i)

# ans = [5, 7, 5, 4]
# out = [5, 5, 7, 4]
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
# %%

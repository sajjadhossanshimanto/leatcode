'''
https://leetcode.com/problems/maximum-frequency-stack/description/
- do i need to do it in O(1) or O(n)
- is their any way to ditermine it????
- the worse codes algo includes usuing max upon dict.values()
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
#%%
# uses hashmap where frequency is the key
# just like adj graph list
from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.freq = {}
        self.freq_map = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        # self.stack.append(val)# do  need that
        self.freq[val] = self.freq.get(val, 0)# default dict
        self.freq[val] += 1
        freq = self.freq[val]

        self.freq_map[freq].append(val)
        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        if self.max_freq==0:
            return 
        
        val = self.freq_map[self.max_freq].pop()
        self.freq[val] -= 1

        while self.max_freq>0 and not self.freq_map[self.max_freq]:
            self.max_freq -=1
        
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

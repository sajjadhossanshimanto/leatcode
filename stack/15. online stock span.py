'''
https://leetcode.com/problems/online-stock-span/
'''
#%%
from typing import List


inf = float('inf')
class StockSpanner:
    def __init__(self):
        self.stock = []# (price, idx)
        self.pos = -1

    def next(self, price: int) -> int:
        self.pos += 1# what's why pos is default to -1
        stock = self.stock
        ans = 1
        while stock and stock[-1][0] <= price:
            ans = self.pos - stock.pop()[1] + 1
        stock.append((price, self.pos))

        return ans

#%%
s = StockSpanner()
l = [100, 80, 60, 70, 60, 75, 85]
for i in l:
    print(s.next(i))
# %%

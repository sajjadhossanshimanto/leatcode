'''
https://leetcode.com/problems/online-stock-span/
- call wold be 10^4 so need `linear` algo
'''
#%%
from typing import List


inf = float('inf')
class StockSpanner:
    def __init__(self):
        self.stock = []# (price, idx)
        self.pos = 0

    def next(self, price: int) -> int:
        self.pos += 1
        stock = self.stock
        ans = 1
        while stock and stock[-1][0] <= price:
            stock.pop()

        if not stock: ans = self.pos
        else:
            ans = self.pos - stock[-1][1]
        stock.append((price, self.pos))

        return ans

#%%
s = StockSpanner()
l = [100, 80, 60, 70, 60, 75, 85]
for i in l:
    print(s.next(i))
# %%

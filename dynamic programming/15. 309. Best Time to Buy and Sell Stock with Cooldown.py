# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

#%%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(level, brought=False):
            # level -> indicate price day
            # brought -> if true can sell
            if level>=len(prices): 
                return 0
            if (level, brought) in cache:
                return cache[(level, brought)]

            pro = 0 
            cooldown  = max(pro, dfs(level+1, brought))# cooldown
            if brought:
                sell  = dfs(level+2, not brought) + prices[level]# sell
                pro = max(cooldown, sell)
            else:# buying
                buy  = dfs(level+1, True) - prices[level]
                pro = max(cooldown, buy)
            
            cache[(level, brought)] = pro
            return pro
        
        return dfs(0)

s = Solution()
# %%
s.maxProfit(
    prices = [1,2,3,0,2]
)
# %%
# ans: 3
s.maxProfit(
    [2,1,4]
)
# %%

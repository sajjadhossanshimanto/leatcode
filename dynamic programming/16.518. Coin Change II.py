# https://leetcode.com/problems/coin-change-ii/description/

#%%
from typing import List
from functools import lru_cache


# when recurtion fails tabulation comes in handy
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        # this is m.n time complexity
        @lru_cache(None)
        def dfs(start=0, money_left=amount):
            if money_left==0: return 1
            if start==len(coins): return 0

            count = 0
            for i in range(start, len(coins)):
                if i>money_left: break

                count+=dfs(i, money_left-coins[i])
            
            return count
        
        return dfs()

s = Solution()
# %%
# ans: 5
# out: 9 as it contain replacement
s.change(
    amount = 5, coins = [5, 2, 1]
)
# %%
s.change(
    amount = 3, coins = [2]
)

#%% tl
s.change(
    amount=4681, coins=[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,166,168,170,172,174,176,178,180,182,184,186,188,190,192,194,196,198,200,202,204,206,208,210,212,214,216,218,220,222,224,226,228,230,232,234,236,238,240,242,244,246,248,250,252,254,256,258,260,262,264,266,268,270,272,274,276,278,280,282,284,286,288,290,292,294,296,298,300,302,304,306,308,310,312,314,316,318,320,322,324,326,328,330,332,334,336,338,340,342,344,346,348,350,352,354,356,358,360,362,364,366,368,370,372,374,376,378,380,382,384,386,388,390,392,394,396,398,400,402,404,406,408,410,412,414,416,418,420,422,424,426,428,430,432,434,436,438,440,442,444,446,448,450,452,454,456,458,460,462,464,466,468,470,472,474,476,478,480,482,484,486,488,490,492,494,496,498,500,502,504,506,508,510,512,514,516,518,520,522,524,526,528,530,532,534,536,538,540,542,544,546,548,550,552,554,556,558,560,562,564,566,568,570,572,574,576,578,580,582,584,586,588,780,936,1170,1560,2340,4680]
)

#%%
# dynamic solution
'''
as our dfs has 2 inputs -> dp array is gooing tobe 2D
2 paramiters of function are `amount`, `coin i`

then 2 side of dp will be amout and coin
as the amount start from 5 and coin with 0'th index
- one side of the dp will be `amount` starting from 5
- another side of the dp will be `coin` starting from index zero
--------------->
| 5 4 3 2 1 0 -> amount
| 1 . . . . .
| 2 . . x . .
| 5 . . . . .
| ↓
| coin
↓
any given point x represents how many ways out there that will make 
that amount using coint bellow that point

amount 0 -> is the base case here
initialise all amount 0 with 1 
--------------->
| 5 4 3 2 1 0 -> amount
| 1 . . . . 1
| 2 . . . . 1
| 5 . . . . 1
| ↓
| coin
↓
our desised ans is the top most upper corner (amout =5, coin index=0)
we can fill the matrix eithter row by row or column by column
### column by column
--------------->            --------------->
| 5 4 3 2 1 0 -> amount     | 5 4 3 2 1 0 -> amount
| 1 . . . . 1               | 1 . . . . 1
| 2 . . . . 1               | 2 . . . x 1
| 5 . . . x 1               | 5 . . . x 1
| ↓                         | ↓
| coin                      | coin
↓

starting with amount (1, 5)
    - we have only one coin to choise 5
    - which will lead us to 1-5= -4 out of boundery so write 0
    ---------------> amount
    | 5 4 3 2 1 0 ->
    | 1 . . . . 1   
    | 2 . . . . 1   
    | 5 . . . 0 1   
    | ↓             
    coin          
then (1, 2)
    - now we have 2 coin to chose from [2, 5]
    - if we choise 2 -> 1-2=-1 out of bounce 
    - but we can also choise from the rest for which we will directly see the bellow index
    ---------------> amount
    | 5 4 3 2 1 0 ->
    | 1 . . . . 1   
    | 2 . . . 0 1   
    | 5 . . . 0 1   
    | ↓             
    coin          
then (1, 1)
    - we choise coin 1-> 1-1=0 which refeers to 1 
    - or we may choise coin from rest of them, for which we just need to watch the bellow row

we will notice for an orbitary index (3, 1)
- if we choise coin 1 our end result 3-1 might end up at any part of the left
- but among the rows bellow we will only need just the bellowth row 

so why not to srink the dp matrix with 2 row just the bollow row with
current row. but current row must have all the rightward value generated

so need to start to solve the row matrix from right side to the left
'''
#%%

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [
            [0]*(amount+1)
            for _ in range(len(coins))
        ]

        # base case
        for i in dp:
            i[0] = 1
        
        for coin_index in range(len(dp)-1, -1, -1):# solving dp row by row from right toward left
            for i in range(1, len(dp[0])):# just reversed the column labelling
                
                # seleting the coin
                if i-coins[coin_index]>=0:# out of boundery check
                    dp[coin_index][i] = dp[coin_index][i-coins[coin_index]]
                
                # seleting rest coins bellow
                if coin_index+1<len(dp):
                    dp[coin_index][i] += dp[coin_index+1][i]

        return dp[0][-1]

#%%
# row reduced space observed solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        below_row = [0]*(amount+1)
        curr_row = [0]*(amount+1)


        # base case
        below_row[0] = 1
        curr_row[0] = 1
        
        for coin_index in range(len(coins)-1, -1, -1):# solving dp row by row from right toward left
            for i in range(1, len(curr_row)):# just reversed the column labelling
                
                # seleting the coin
                if i-coins[coin_index]>=0:# out of boundery check
                    curr_row[i] = curr_row[i-coins[coin_index]]
                # seleting rest coins bellow
                curr_row[i] += below_row[i]
            
            below_row = curr_row
            curr_row = [0]*(amount+1)
            curr_row[0] = 1
        
        # actually rest is current row but reseted by end lines of for loop
        # and now array below row cointain backup of curr_row
        return below_row

s = Solution()
s.change(
    amount = 5, coins = [5, 2, 1]
)
# %%

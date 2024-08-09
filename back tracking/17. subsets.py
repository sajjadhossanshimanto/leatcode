'''
https://leetcode.com/problems/subsets/submissions/1341623331/
- this is how a subset is constracted
- for each element we have 2 choises. 
    1. add one 
    2. not add that
-  this is why for a set of len 3 -> [1, 2, 3] -> subset 2*2*2 ==> 2^n
- this logic would be the core of `decition tree`
'''
#%%
from typing import List
from itertools import combinations


class Solution:
    # complexity -> O(2^N) TODO: how something can be 2^n
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for ln in range(1, len(nums)):
            ans.extend(combinations(nums, r=ln))

        ans.append(nums)
        return ans

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        temp = []
        def dfs(i):
            if i == len(nums):
                # icomparing a num with len(list)
                # this checkes clearify we have reached end of tree
                res.append(temp[:])
                return
            
            # decision to include nums[i]
            temp.append(nums[i])
            dfs(i+1)
            
            # decision to ==NOT== include nums[i]
            temp.pop()
            dfs(i+1)
            # these call may look the same but
            # - forst dfs would have dfs with i included
            # - 2nd one with have empty set given to it


        dfs(0)
        return res

# %%
# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# return type not nececeruly have tobe list[list], list[tupe] also ok
Solution().subsets([1, 2, 3])
# %%
Solution().subsets([0])
# %%

#%%
from typing import List
from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = tuple(sorted(nums))
        ans = {tuple()}
        for ln in range(1, len(nums)):
            ans.update(combinations(nums, r=ln))

        ans.add(nums)
        return ans

#%%
# from solution
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # memorising the path we are going through
        def backtrack(i, path):
            res.append(path)
            for j in range(i, len(nums)):
                # as nums sorted all duplicates are adjecent
                if j > i and nums[j] == nums[j-1]: continue
                backtrack(j+1, path+[nums[j]])
        backtrack(0, [])
        return res

# %%
Solution().subsetsWithDup([1, 2, 3])
# %%
Solution().subsetsWithDup([1, 2, 2])
# %%
Solution().subsetsWithDup([0])
# %% wa 15
# ans = [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
# out = [[],[1],[4,4],[4,4,1,4],[4,4,4,4],[4,1,4],[4,4,1],[4],[1,4],[4,4,4],[4,4,4,1,4],[4,1],[4,4,4,1]]
Solution().subsetsWithDup([4,4,4,1,4])
# %%
def combinations(n, r):
  """Generates combinations of r elements from a set of n elements.

  Args:
    n: Total number of elements.
    r: Number of elements to choose.
  """

  if r > n:
    return  # Invalid input: r cannot be greater than n

  # Initial combination indices
  indices = list(range(r))

  while True:
    # Print the current combination (for debugging or testing)
    print(indices)

    # Find the rightmost index that can be incremented
    for i in reversed(range(r)):
      if indices[i] != i + (n - r):
        break
    else:
      # All indices are at their maximum, no more combinations
      return

    # Increment the selected index
    indices[i] += 1

    # Adjust subsequent indices
    for j in range(i + 1, r):
      indices[j] = indices[j - 1] + 1


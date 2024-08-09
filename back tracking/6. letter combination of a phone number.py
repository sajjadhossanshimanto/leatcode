'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
#%%
from typing import List
from itertools import permutations

key_map = {
    '2':["a", "b", "c"],
    '3':["d", "e", "f"],
    '4':["g", "h", "i"],
    '5':["j", "k", "l"],
    '6':["m", "n", "o"],
    '7':["p", "q", "r", "s"],
    '8':["t", "u", "v"],
    '9':["w", "x", "y", "z"]
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        ans = []

        n = len(digits)
        boundery = []
        # letters = []
        for i in digits:
            boundery.append(len(key_map[i]))
        
        index = [0]*n
        ans.append("".join(key_map[digits[i]][index[i]] for i in range(n)))

        while True:            
            for i in range(n-1, -1, -1):
                # if in boundery
                if index[i]>=boundery[i]-1: # if == that leans out of boundery
                    continue

                index[i]+=1
                for j in range(i+1, n):
                    index[j] = 0
                
                ans.append("".join(key_map[digits[i]][index[i]] for i in range(n)))
                break
            else:
                return ans

s = Solution()
# %%
s.letterCombinations("234")
# %%
def combination(n):
    index = [0]*n
    boundery = [1, 2, 3]*n

    print(index)
    while True:
        for i in range(n-1, -1, -1):
            # if in boundery
            if index[i]>=boundery[i]-1: # if == that leans out of boundery
                continue

            index[i]+=1
            for j in range(i+1, n):
                # index[j] = index[j-1] + 1
                index[j] = 0
            print(index)
            break
        else:
            return

# %%
com(3)
# %%

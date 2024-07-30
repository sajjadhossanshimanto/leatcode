'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
'''
#%%
from typing import List


inf = float('inf')
class Solution:
    def removeDuplicates(self, s: str, k: int) -> int:
        i = 0
        while len(s)>=k and i!=len(s)-1:
            char = s[i]
            for j in range(i+1, i+k):# forward checking
                # as `i+k` is unsecuire
                if j<len(s) and s[j]!=char:
                    i = j
                    break

            if j-i+1==k:# if not breaked. +1 for including both end-point
                s = "".join([s[:i], s[j+1:]])
                # back steping
                while i-1>=0 and s[i]==s[i-1]:
                    i-=1

        return s

class Solution:
    def removeDuplicates(self, s: str, k: int) -> int:
        def plus_string(*arg):
            return "".join(arg)

        def slice_s(start, end, s):
            '''both end points are included'''
            return plus_string([s[:start], s[end+1:]])

        def forward_match(char, start, step):
            '''
            returns: bool if all matches otherwise int:pos where it mismatches
            disclimer: 1==True: true
            '''
            for j in range(start, start+step):
                # as `start+step` can go out of boundry
                if j<len(s) and s[j]!=char:
                    return j
            return True

        repeat = ['0']*len(s)
        i = 0
        while len(s)>=k and i!=len(s)-1:
            char = s[i]
            # forward checking frpm i+1 to i+k with i
            j = forward_match(char, i+1, k)
            if isinstance(j, int):
                repeat[j] = j-i# TODO
                i=j
            else:
                s = slice_s(i, i+k, s)
                # now in place of i new char will come
                # back checking
                while s[i-1]==s[i]:
                    r = int(repeat[i-1])
                    if r+1:# 1 for current i
                        s = slice_s(i-k, i, s)
                    elif 


            if j-i+1==k:# if not breaked. +1 for including both end-point
                s = slice_s(i, j, s)
                # back steping
                while i-1>=0 and s[i]==s[i-1]:
                    i-=1

        return s

s = Solution()
# %%
# ans = "abcd"
s.removeDuplicates(s = "abcd", k = 2)
# %%
# ans = "aa"
s.removeDuplicates(s = "deeedbbcccbdaa", k = 3)
# %%
# ans = "ps"
s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2)
# %%

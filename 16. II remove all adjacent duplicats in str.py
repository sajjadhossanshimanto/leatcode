#TODO: check I'th question
#%%
from typing import List


inf = float('inf')
class Solution:
    def removeDuplicates(self, s: str, k: int) -> int:
        parent = [-1]*len(s)
        def find(a: int):
            # if parent[a]==-1:
            #     return 
            if parent[a]<0: return a

            r = find(parent[a])
            parent[a] = r
            return r

        remove = []
        def union(a:int, b:int):
            ''' make a as parent unconditionally '''
            p1 = find(a)
            p2 = find(b)
            parent[p1] += parent[p2]
            parent[p2] = p1
            # union node count has reached the limit
            # remove.append((p1, b))# from b to the start
            # TODO how am i gona remove it

        ans = s
        i = 1
        while i!=len(s):
            if s[i]==s[i-1]:
                union(i-1, i)
                # as after this 
                p1 = find(i-1)
                if abs(parent[p1])==k:
                # remove from p1 to i/ can be said as p1+i
                    s = "".join([s[:p1], s[p1+k+1:]])
                    for j in range(p1, p1+k):
                        parent[j] = -1
                        parent.pop()
                    i=p1#TODO: should i -1 to p1
            else:
                i+=1
        
        return s

s = Solution()
# %%
s.removeDuplicates("deeedbbcccbdaa", k=3)
# %%

#%%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#%% 
def list_to_link(l):
    head = None
    node = None
    for i in l:
        n = ListNode(i)
        if not node:
            head = n
            node = n
        else:
            node.next = n
            node = n

    return head

# %%
def print_link(ans):
    l = []
    while ans:
        l.append(ans.val)
        ans = ans.next
    print(l)
    return l

# %%
# l = [1, 2, 3, 4, 5]
# head = list_to_link(l)
# print_link(ans)
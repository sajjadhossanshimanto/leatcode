#%%
from collections import defaultdict, deque
from random import randint

import matplotlib.pyplot as plt
import networkx as nx

from networkx.drawing.nx_pydot import graphviz_layout


G = nx.DiGraph()

labels = {}
def process_tree(tree):
    G.clear()
    c = 1
    labels[c] = tree.val

    etu = [tree.val]
    q = deque([[tree, c]])
    while q:
        node, c = q.popleft()

        etu.append(None)
        if node.left!=None:
            pos = c+1
            if q:
                pos = q[-1][1] + 1
            G.add_edge(c, pos)
            labels[pos] = node.left.val

            q.append((node.left, pos))
            etu[-1] = node.left.val
        
        etu.append(None)
        if node.right!=None:
            pos = c+1
            if q:
                pos = q[-1][1] + 1
            G.add_edge(c, pos)
            labels[pos] = node.right.val

            q.append((node.right, pos))
            etu[-1] = node.right.val

    while etu[-1]==None:
        etu.pop()
    
    return etu

def draw_graph(cache=True, seed=None):
    ''' 
    - use `cache=False` to forcefully redraw 
    ~ - if you use `seed must enable redrawing`
    '''
    pos = graphviz_layout(G, prog="dot")
    # pos = nx.spring_layout(G)

    # nodes with level
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos, labels)

    # edges -> straight
    nx.draw_networkx_edges(G, pos)
    
    plt.show()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def etu_to_tree(nums):
    
    def dfs(i):
        if not 0<i<=len(nums):
            return 
        if nums[i-1] == None:
            return None

        # i is 1 indexed
        node = TreeNode(nums[i-1])
        node.left = dfs(2*i)
        node.right = dfs(2*i+1)

        return node
    
    return dfs(1)

if __name__=="__main__":
    t = [1,2,3,4,5,6,None, None, 6]
    t = etu_to_tree(t)
    print(process_tree(t))
    # %%
    draw_graph()
# %%

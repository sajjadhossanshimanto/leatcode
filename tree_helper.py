from collections import defaultdict
from random import randint

import matplotlib.pyplot as plt
import networkx as nx



G = nx.DiGraph()

def process_tree(tree):
    G.clear()

    def dfs(node):
        if node.right!=None:
            G.add_edge(node.val, node.right.val)
            dfs(node.right)
        if node.left!=None:
            G.add_edge(node.val, node.left.val)
            dfs(node.left)

    dfs(tree)

pos = None
def draw_graph(cache=True, seed=None):
    ''' 
    - use `cache=False` to forcefully redraw 
    ~ - if you use `seed must enable redrawing`
    '''
    # subax1 = plt.subplot(121)
    global pos

    if seed:
        pos = nx.spring_layout(G, seed=seed)
    elif (not cache) or (not pos):
        seed = randint(1000, 9999)
        print(f"seed = {seed}")
        pos = nx.spring_layout(G, seed=seed)

    # nodes with level
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)

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

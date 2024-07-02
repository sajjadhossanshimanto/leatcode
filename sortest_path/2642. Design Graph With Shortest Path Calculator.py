#%%
from heapq import heappush, heappop

#%%

adj = graph_input(inp, 1, 1)
draw_graph(0, 1, 1)

#%%
class Graph:

    def __init__(self, n: int, edges):
        self.adj = [[] for _ in range(n)]
        self.n = n
        for edge in edges: self.addEdge(edge)

        # my defined
        self.last_search = -1# cache
        self.sssp =[]

    def addEdge(self, edge) -> None:
        a, b, w = edge
        self.adj[a].append([b, w])
        self.last_search = -1 #clear cache

    def dijksta(self, node):
        pq = []
        heappush(pq, (0, node))
        while pq:
            dis, node = heappop(pq)
            if dis> self.sssp[node]: continue
            for child, w in self.adj[node]:
                nd = dis+w
                if nd>self.sssp[child]: continue
                self.sssp[child] = nd
                heappush(pq, (nd, child))

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1==self.last_search:
            return self.sssp[node2]

        self.sssp = [float('inf')]*self.n
        self.sssp[node1] = 0
        self.dijksta(node1)
        
        if self.sssp[node2]==float("inf"):
            return -1
        return self.sssp[node2]

#%%
g = Graph(4, [[0,2,5],[0,1,2],[1,2,1],[3,0,3]])
print(g.shortestPath(3, 2))
print(g.shortestPath(0, 3))
print(g.addEdge([1, 3, 4]))
print(g.shortestPath(0, 3))
# %%
l=[[7,2,131570],[9,4,622890],[9,1,812365],[1,3,399349],[10,2,407736],[6,7,880509],[1,4,289656],[8,0,802664],[6,4,826732],[10,3,567982],[5,6,434340],[4,7,833968],[12,1,578047],[8,5,739814],[10,9,648073],[1,6,679167],[3,6,933017],[0,10,399226],[1,11,915959],[0,12,393037],[11,5,811057],[6,2,100832],[5,1,731872],[3,8,741455],[2,9,835397],[7,0,516610],[11,8,680504],[3,11,455056],[1,0,252721]]
g = Graph(13,l)
print(g.shortestPath(9,3))

#%%
from Graph.store_graph import draw_graph, graph_input, build_plotly
inp = ''
for i in l:
    inp=inp+" ".join(map(str, i))+"\n"

graph_input(inp, 1, 1)
draw_graph(0, 1, 1, seed = 9066)
# build_plotly()

#%%
print(g.shortestPath(9,3))
print(g.addEdge([11,1,873094]))
print(g.shortestPath(3,10))
print(g.addEdge([0,9,601498]))
print(g.addEdge([12,0,824080]))
print(g.addEdge([12,4,459292]))
print(g.addEdge([6,9,7876]))
print(g.addEdge([11,7,5479]))
print(g.addEdge([11,12,802]))
print(g.shortestPath(2,9))
print(g.shortestPath(2,6))
print(g.addEdge([0,11,441770]))
print(g.shortestPath(3,7))
print(g.addEdge([11,0,393443]))
print(g.shortestPath(4,2))
print(g.addEdge([10,5,338]))
print(g.addEdge([6,1,305]))
print(g.addEdge([5,0,154]))

# %%
# output = [null,-1,null,-1,null,null,null,null,null,null,835397,-1,null,460535,null,965538,null,null,null]...
# expect = [null,1211714,null,1943345,null,null,null,null,null,null,835397,2326929,null,460535,null,965538,null,null,null]...
from collections import defaultdict
from heapq import heappop, heappush 

class Graph(object): 
    """ 
    隣接リストによる有向グラフ
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):
    """
    ダイクストラ法（二分ヒープ）による最短経路探索
    計算量: O((E+V)logV)
    """

    def __init__(self, graph, start):
        self.g = graph.graph

        # startノードからの最短距離
        # startノードは0, それ以外は無限大で初期化
        self.dist = defaultdict(lambda: float('inf'))
        self.dist[start] = 0

        # 最短経路での1つ前のノード
        self.prev = defaultdict(lambda: None)

        # startノードをキューに入れる
        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            # 優先度（距離）が最小であるキューを取り出す
            dist_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    def shortest_distance(self, goal):
        """
        startノードからgoalノードまでの最短距離
        """
        return self.dist[goal]

    def shortest_path(self, goal):
        """
        startノードからgoalノードまでの最短経路
        """
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


n, m = map(int,input().split())
inputs =[]


inputs = [[0,0,0]*m]
for i in range(m):
    a,b,c = map(int,input().split())
    inputs.append((a,b,c))

g = Graph()
for src, dst, weight in inputs:
    g.add_edge(src, dst, weight)
    g.add_edge(dst, src, weight)


lst = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i != j:
            d = Dijkstra(g, i)
            lst[i][j]= d.shortest_distance(j)

ans =0
for i in range(m):
    if lst[inputs[i][0]][inputs[i][1]] < inputs[i][2]:
        ans+=1

print(ans)

    


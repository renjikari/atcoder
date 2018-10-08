from collections import defaultdict
from heapq import heappop, heappush

class Graph(object):
    """
    隣接リストによる有向グラフ
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))


class Dijkstra(object):
    """
    ダイクストラ法（二分ヒープ）による最短経路探索
    計算量: O((E+V)logV)
    """

    def __init__(self, inputs,m, start):
        #self.graph = defaultdict(list)
        self.graph = [ [[0, 0] for i in range(n+1)] for j in range(n+1)]
        #lst = [[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(m):
            self.graph[inputs[i][0]]=[inputs[i][1], inputs[i][2]]
            self.graph[inputs[i][1]]=[inputs[i][0], inputs[i][2]]
            #self.graph[inputs[i][0]].append((inputs[i][1], inputs[i][2]))
            #self.graph[inputs[i][1]].append((inputs[i][0], inputs[i][2]))

        self.g = self.graph

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

def main():
    n, m= map(int,input().split())
    g = Graph()

    inputs = [0]*m

    for i in range(m):
        lst = [int(i) for i in input().split()]
        inputs[i]=lst

    lst = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i != j and lst[j][i] == 0:
                d = Dijkstra(inputs,m,i)
                lst[i][j] = d.shortest_distance(j)

   # print(lst)
    #print(inputs)

    ans = 0
    for i in range(1,m):
        if lst[min(inputs[i][0],inputs[i][1])][max(inputs[i][0],inputs[i][1])] < inputs[i][2]:
            ans+=1

    print(ans)

if __name__ == "__main__":
        main()















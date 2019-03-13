from collections import defaultdict
from heapq import heappop, heappush
from collections import Counter

def main():
    n,s,t = map(int,input().split())
    c = list(map(int,input().split()))

    lst = [0 for i in range(n-1)]
    for i in range(n-1):
        lst[i] = list(map(int,input().split()))

    g=Graph()
    for src, dst in lst:
        g.add_edge(src,dst)
        g.add_edge(dst,src)

    d=Dijkstra(g,s)

    ans_lst=[]
    print(d.shortest_path(t))
    for i in d.shortest_path(t):
        ans_lst.append(c[i-1])
    print(ans_lst)

    c = Counter(ans_lst)
    print(c.most_common()[0][0])


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):
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
        return self.dist[goal]

    def shortest_path(self, goal):
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]


if __name__ == "__main__":
        main()



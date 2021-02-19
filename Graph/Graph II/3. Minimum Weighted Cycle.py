from collections import defaultdict
from heapq import *

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, i, j, k):
        self.graph[i].append((j, k))
        self.graph[j].append((i, k))

    def removeEdge(self, i, j, k):
        self.graph[i].remove((j, k))
        self.graph[j].remove((i, k))

    def cycle(self, A, u, v):
        dis = [float('inf') for _ in range(A)]
        dis[u] = 0
        pq = []
        heappush(pq, (0, u))

        while pq:
            wt, node = heappop(pq)
            for nxt_node, w in self.graph[node]:
                new_dis = wt + w
                if new_dis < dis[nxt_node]:
                    dis[nxt_node] = new_dis
                    heappush(pq, (new_dis, nxt_node))

        return dis[v]

    def solve(self, A, B):
        for i, j, k in B:
            self.addEdge(i-1, j-1, k)

        ans = float('inf')
        for i, j, k in B:
            self.removeEdge(i-1, j-1, k)
            val = self.cycle(A, i-1, j-1)
            ans = min(ans, val + k)

        return ans


if __name__ == '__main__':
    A = 4
    B = [[1, 2, 2],
         [2, 3, 3],
         [3, 4, 1],
         [4, 1, 4],
         [1, 3, 15]]
    C = Solution()
    print(C.solve(A, B))

from collections import defaultdict


class Solution:
    def dfs(self, v, k, vis):
        vis.add(v)
        if not k:
            return

        for w in self.graph[v]:
            if w not in vis:
                vis.add(w)
                self.ans = 0
                self.dfs(w, k-1, vis)


    def solve(self, A, B, C):
        self.graph = defaultdict(list)
        self.ans = float('inf')

        for i, j in enumerate(B):
            self.graph[j].append((i+1, abs(C[j-1] - C[i])))

        self.graph.pop(0)

        return self.graph


if __name__ == '__main__':
    A = 3
    B = [0, 1, 1, 2, 2, 3]
    C = [1, 6, 7, 21, 5, 18]
    D = Solution()
    print(D.solve(A, B, C))

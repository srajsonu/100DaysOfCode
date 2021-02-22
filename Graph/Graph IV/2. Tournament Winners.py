from collections import defaultdict


class Solution:
    def dfs(self, v, vis):
        vis.add(v)
        self.cnt += 1
        for w in self.graph[v]:
            if w not in vis:
                vis.add(w)
                self.dfs(w, vis)

    def solve(self, A, B):
        self.graph = defaultdict(list)
        m = len(B)
        n = len(B[0])

        for i in range(m):
            for j in range(n):
                if B[i][j] == 1:
                    self.graph[i].append(j)

        ans = 0
        for i in range(A):
            vis = set()
            self.cnt = 0
            self.dfs(i, vis)
            if self.cnt == A:
                ans += 1

        return ans


if __name__ == '__main__':
    A = 4
    B = [[0, 1, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]
    C = Solution()
    print(C.solve(A, B))

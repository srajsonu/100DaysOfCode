from collections import defaultdict


class Solution:
    def dfs(self, A, i, vis):
        vis.add(i)
        for j in self.graph[i]:
            if j not in vis:
                vis.add(j)
                self.dfs(A, j, vis)

    def solve(self, A, B, C):
        self.graph = defaultdict(list)

        for i, j in enumerate(A):
            self.graph[i+1].append(A[i])

        vis = set()
        self.dfs(A, B, vis)

        return 1 if C in vis else 0

if __name__ == '__main__':
    A = [1, 1, 2]
    B = 2
    C = 1
    D = Solution()
    print(D.solve(A, B, C))

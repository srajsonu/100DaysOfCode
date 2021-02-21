from collections import defaultdict


class Solution:
    def dfs(self, B, v, vis, xor):
        vis.add(v)
        xor[v] = B[v]

        for w in self.graph[v]:
            if w not in vis:
                vis.add(w)
                self.dfs(B, w, vis, xor)
                xor[v] ^= xor[w]

    def solve(self, A, B, C):
        self.graph = defaultdict(list)

        for i, j in C:
            self.graph[i].append(j)
            self.graph[j].append(i)

        vis = set()
        xor = [0 for _ in range(A)]
        self.dfs(B, 0, vis, xor)

        ans = max(xor)
        cnt = 0
        for i in xor:
            if i == ans:
                cnt += 1

        return [ans, cnt]



if __name__ == '__main__':
    A = 5
    B = [11, 10, 12, 12, 7]
    C = [[0, 4],
         [1, 0],
         [1, 3],
         [3, 2]]
    D = Solution()
    print(D.solve(A, B, C))

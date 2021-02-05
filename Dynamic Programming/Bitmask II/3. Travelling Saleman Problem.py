from collections import defaultdict


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def cnt_bits(self, mask):
        cnt = 0
        for i in range(32):
            if (mask >> i) & 1:
                cnt += 1
        return cnt

    def dp(self,A, node, mask, dp):
        vis_city = self.cnt_bits(mask)
        if vis_city == A:
            return self.B[node][0]

        if (node, mask) in dp:
            return dp[(node, mask)]

        ans = float('inf')
        for nxt_node, cost in self.graph[node]:
            if (mask >> nxt_node) & 1:
                continue

            ans = min(ans, cost + self.dp(A, nxt_node, mask | (1 << nxt_node), dp))

        dp[(node, mask)] = ans
        return ans

    def solve(self, A, B):
        self.B = B
        m = len(B)
        n = len(B[0])
        for i in range(m):
            for j in range(n):
                if B[i][j] == 0: continue
                self.graph[i].append((j, B[i][j]))

        dp = {}
        return self.dp(A, 0, 1, dp)



if __name__ == '__main__':
    A = 3
    B = [[0, 500, 100],
         [100, 0, 500],
         [500, 100, 0]]
    C = Solution()
    print(C.solve(A, B))

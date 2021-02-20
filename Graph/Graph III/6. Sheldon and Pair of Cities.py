class Solution:
    def solve(self, A, B, C, D, E, F, G, H):
        dp = [[float('inf') for _ in range(A)] for _ in range(A)]

        for i, j, k in zip(D, E, F):
            dp[i-1][j-1] = k
            dp[j-1][i-1] = k

        for i in range(A):
            dp[i][i] = 0

        for k in range(A):
            for i in range(A):
                for j in range(A):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        ans = []
        for i, j in zip(G, H):
            if dp[i-1][j-1] == float('inf'):
                ans.append(-1)
            else:
                ans.append(dp[i-1][j-1])

        return ans



if __name__ == '__main__':
    A = 4
    B = 6
    C = 2
    D = [1, 2, 3, 2, 4, 3]
    E = [2, 3, 4, 4, 1, 1]
    F = [4, 1, 1, 1, 1, 1]
    G = [1, 1]
    H = [2, 3]
    I = Solution()
    print(I.solve(A, B, C, D, E, F, G, H))

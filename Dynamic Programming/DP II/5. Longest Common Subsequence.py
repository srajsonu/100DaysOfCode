import sys
sys.setrecursionlimit(10 ** 9)
class Solution:
    def dp(self, A, B, i, j, dp):
        ans = 0
        if dp[i][j]:
            return dp[i][j]

        if i == 0 or j == 0:
            ans = 0

        elif A[i] == B[j]:
            ans = 1 + self.dp(A, B, i-1, j-1, dp)
        else:
            ans = max(self.dp(A, B, i, j-1, dp), self.dp(A, B, i-1, j, dp))

        dp[i][j] = ans
        return ans

    def solve(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        return self.dp(A, B, m-1, n-1, dp)

    def lcs(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in  range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                elif A[i] == B[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]


if __name__ == '__main__':
    A = "abbcdgf"
    B = "bbadcgf"
    C = Solution()
    print(C.solve(A, B))
    print(C.lcs(A, B))

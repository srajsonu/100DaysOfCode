import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def dp(self, A, B, i, j, dp):
        global ans
        if dp[i][j] != -1:
            return dp[i][j]

        if i == 0 and j == 0:
            return 1

        if i == 0 or j == 0:
            if j == 0:
                ans = 1
            else:
                ans = 0

        elif A[i] == B[j]:
            ans = self.dp(A, B, i-1, j-1, dp) + self.dp(A, B, i-1, j, dp)
        else:
            ans = self.dp(A, B, i-1, j, dp)

        dp[i][j] = ans
        return ans

    def numDistinct(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dp(A, B, m-1, n-1, dp)

    def solve(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 or j == 0:
                    if i == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                elif A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]


if __name__ == '__main__':
    A = "abc"
    B = "abc"
    C = Solution()
    print(C.numDistinct(A, B))
    print(C.solve(A, B))

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

if __name__ == '__main__':
    A = "rabbbit"
    B = "rabbit"
    C = Solution()
    print(C.numDistinct(A, B))

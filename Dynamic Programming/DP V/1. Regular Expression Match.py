class Solution:
    def dp(self, A, B, i, j, dp):
        ans = 0
        if dp[i][j] != -1:
            return dp[i][j]

        if i == 0 and j == 0:
            return 1

        elif i == 0 or j == 0:
            if B[j] == '*':
                ans = self.dp(A, B, i, j-1, dp)
            else:
                ans = 0

        elif A[i] == B[j] or B[j] == '?':
            ans = self.dp(A, B, i-1, j-1, dp)

        elif B[j] == '*':
            ans = self.dp(A, B, i-1, j, dp) or self.dp(A, B, i, j-1, dp)

        dp[i][j] = ans
        return ans

    def isMatch(self, A, B):
        m = len(A)
        n = len(B)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        return self.dp(A, B, m-1, n-1, dp)

    def solve(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1] or B[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

                elif B[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]

if __name__ == '__main__':
    A = "_aaa"
    B = "_a*"
    C = Solution()
    print(C.isMatch(A, B))
    print(C.solve(A, B))

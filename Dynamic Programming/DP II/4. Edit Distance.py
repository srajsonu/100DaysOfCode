class Solution:
    def dp(self, A, B, i, j, dp):
        ans = 0
        if dp[i][j]:
            return dp[i][j]

        if i == 0:
            return j

        elif j == 0:
            return i

        elif A[i] == B[j]:
            ans = self.dp(A, B, i - 1, j - 1, dp)
        else:
            x = self.dp(A, B, i, j - 1, dp)
            y = self.dp(A, B, i - 1, j, dp)
            z = self.dp(A, B, i - 1, j - 1, dp)
            ans = 1 + min(x, y, z)

        dp[i][j] = ans
        return ans

    def minDistance(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        return self.dp(A, B, m - 1, n - 1, dp)

    def solve(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if i == 0 or j == 0:
                    if i == 0:
                        dp[i][j] = j
                    else:
                        dp[i][j] = i

                elif A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    A = 'abaabbbbabaabaa'
    B = 'aaaababa'
    C = Solution()
    print(C.minDistance(A, B))
    print(C.solve(A, B))

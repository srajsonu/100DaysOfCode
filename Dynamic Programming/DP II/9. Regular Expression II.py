import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def dp(self, A, B, i, j, dp):
        print(i, j)
        ans = 0
        if dp[i][j] != -1:
            return dp[i][j]

        if i == 0 and j == 0:
            ans = 1

        elif j == 0:
            ans = 0

        elif A[i] == B[j] or B[j] == '.':
            ans = self.dp(A, B, i-1, j-1, dp)

        elif B[j] == '*':
            ans = self.dp(A, B, i, j-2, dp)
            if B[j-1] == '.' or A[i] == B[j-1]:
                ans = self.dp(A, B, i-1, j, dp)

        dp[i][j] = ans
        return ans

    def isMatch(self, A, B):
        A = '_' + A
        B = '_' + B
        m = len(A)
        n = len(B)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.dp(A, B, m-1, n-1, dp)

if __name__ == '__main__':
    A = "ab"
    B = ".*"
    C = Solution()
    print(C.isMatch(A, B))

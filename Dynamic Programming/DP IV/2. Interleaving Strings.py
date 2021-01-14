import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def dp(self, A, B, C, i, j, k, dp):
        global ans
        if i == 0 and j != 0 and k == 0:
            return A[i] == C[k]

        if i != 0 and j == 0 and k == 0:
            return B[j] == C[k]

        if (i, j, k) in dp:
            return dp[(i, j, k)]

        if A[i] == C[k] and B[j] == C[k]:
            ans = self.dp(A, B, C, i-1, j, k-1, dp) or self.dp(A, B, C, i, j-1, k-1, dp)
        elif A[i] == C[k] and B[j] != C[k]:
            ans = self.dp(A, B, C, i-1, j, k-1, dp)
        elif A[i] != C[k] and B[j] == C[k]:
            ans = self.dp(A, B, C, i, j-1, k-1, dp)
        else:
            ans = 0

        dp[(i, j, k)] = ans
        return ans

    def isInterleave(self, A, B, C):
        l = len(A)
        m = len(B)
        n = len(C)
        if l+m != n: return 0
        dp = {}
        return self.dp(A, B, C, l-1, m-1, n-1, dp)

    def solve(self, A, B, C):
        l = len(A)
        m = len(B)
        n = len(C)
        if l + m != n: return 0
        dp = {}

        for i in range(l):
            for j in range(m):
                for k in range(n):
                    pass


if __name__ == '__main__':
    A = "aabcc"
    B = "dbbca"
    C = "aadbbcbcac"
    D = Solution()
    print(D.isInterleave(A, B, C))

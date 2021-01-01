class Solution:
    def dp(self, A, B, i, j, dp):
        ans = 0
        if i == 0 and j == 0:
            return 1

        if i == 0 or j == 0:
            return 0

        if A[i] == B[j] or B[j] == '.':
            ans = self.dp(A, B, i-1, j-1, dp)
        elif B[j] == '*':
            ans = self.dp(A, B, i-1, j-1, dp) or self.dp(A, B, i, j-1, dp)

        return ans

    def isMatch(self, A, B):
        A = ' ' + A
        B = ' ' + B
        m = len(A)
        n = len(B)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        return self.dp(A, B, m-1, n-1, dp)

if __name__ == '__main__':
    A = "aab"
    B = "c*a*b"
    C = Solution()
    print(C.isMatch(A, B))

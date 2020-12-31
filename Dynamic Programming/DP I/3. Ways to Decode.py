class Solution:
    def dp(self, s, i, dp):
        global ans
        if dp[i]:
            return dp[i]
        if i == len(s):
            return 1

        if s[i] == '0':
            return 0

        w1 = self.dp(s, i+1, dp)
        w2 = 0
        if i < len(s-1) and int(s[i:i+2]) <= 26 and int(s[i:i+2]) > 0:
            w2 = self.dp(s,i+2, dp)

        dp[i] = w1 + w2
        return dp[i]

    def numDecodings(self, s):
        n = len(s)
        dp = [0 for _ in range(n+1)]
        return self.dp(s, 0, dp)

    def solve(self, A):
        if not A: return 0
        if A[0] == '0': return 0
        n = len(A)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n):
            if A[i-1] >= '1' and A[i-1] <= '9':
                dp[i] = dp[i-1]

            if A[i-2] == '1':
                dp[i] += dp[i-2]

            elif A[i-2] == '2' and A[i-1] >= '0' and A[i-1] <= '6':
                dp[i] += dp[i-2]

        return dp[n]

if __name__ == '__main__':
    A = '126'
    B = Solution()
    print(B.solve(A))
    print(B.numDecodings(A))

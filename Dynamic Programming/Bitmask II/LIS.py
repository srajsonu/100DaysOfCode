class Solution:
    def dp(self, A, pos, last, dp):
        if pos == len(A):
            return 0

        if dp[pos][last] != -1:
            return dp[pos][last]

        ans = self.dp(A, pos+1, last, dp)
        if A[last] < A[pos]:
            ans = max(ans, 1 + self.dp(A, pos+1, pos, dp))

        dp[pos][last] = ans
        return ans

    def prints(self, A, pos, last, dp):
        if pos == len(A):
            print()

        ans = self.dp(A, pos+1, last, dp)
        taken = False

        if A[last] < A[pos]:
            if ans < self.dp(A, pos+1, pos, dp):
                ans = self.dp(A, pos+1, pos, dp)
                taken = True
        if not taken:
            self.prints(A, pos+1, last, dp)
        else:
            print(A[pos])
            self.prints(A, pos+1, pos, dp)

    def solve(self, A):
        n = len(A)
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return self.prints(A, 1, 0, dp)

if __name__ == '__main__':
    A = [2, 1, 3, 4]
    B = Solution()
    print(B.solve(A))

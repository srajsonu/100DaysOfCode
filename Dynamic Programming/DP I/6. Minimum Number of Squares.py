import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def dp(self, n, dp):
        if n <= 1:
            dp[n] = n
            return n

        if dp[n]:
            return dp[n]

        ans = float('inf')
        for i in range(1, n+1):
            tmp = i * i
            if tmp > n:
                break

            ans = min(ans, 1 + self.dp(n - tmp, dp))

        dp[n] = ans
        return ans

    def solve(self, A):
        dp = [0 for _ in range(A+1)]
        return self.dp(A, dp), dp

    def countMinSquares(self, A):
        dp = [0, 1, 2, 3]
        for i in range(4, A+1):
            dp.append(i)
            m = int(i ** 0.5) + 1
            for j in range(1, m):
                tmp = j * j
                if tmp > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i - tmp])

        return dp[A]



if __name__ == '__main__':
    A = 41
    B = Solution()
    print(B.solve(A))
    print(B.countMinSquares(A))

class Solution:
    def cnt_bits(self, mask):
        cnt = 0
        for i in range(32):
            if (mask >> i) & 1:
                cnt += 1
        return cnt

    def dp(self, A, B, mask, dp):
        row = self.cnt_bits(mask)
        if row == len(A):
            return 0

        if dp[row][mask] != -1:
            return dp[row][mask]

        ans = float('inf')
        for col in range(len(B)):
            if (mask >> col) & 1:
                continue

            ans = min(ans, (A[row] ^ B[col]) + self.dp(A, B, mask | (1 << col), dp))

        dp[row][mask] = ans
        return ans

    def solve(self, A, B):
        m = len(A)
        n = pow(2, m)
        dp = [[-1 for _ in range(n)] for _ in range(m+1)]
        return self.dp(A, B, 0, dp), dp

if __name__ == '__main__':
    A = [1, 2, 3, 5]
    B = [1, 2, 3, 4]
    C = Solution()
    print(C.solve(A, B))

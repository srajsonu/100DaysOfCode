class Solution:
    def cnt_bits(self, mask):
        cnt = 0
        for i in range(32):
            if (mask >> i) & 1:
                cnt += 1
        return cnt

    def dp(self, A, mask, dp):
        row = self.cnt_bits(mask)

        if row == len(A):
            return 0

        if (row, mask) in dp:
            return dp[(row, mask)]

        ans = float('-inf')
        for col in range(len(A[row])):
            if (mask >> col) & 1:
                continue

            ans = max(ans, A[row][col] + self.dp(A, mask | (1 << col), dp))

        dp[(row, mask)] = ans
        return ans

    def solve(self, A):
        dp = {}
        return self.dp(A, 0, dp)

if __name__ == '__main__':
    A = [[5, 50],
         [100, 10]]
    B = Solution()
    print(B.solve(A))

class Solution:
    def cnt_bits(self, mask):
        cnt = 0
        for i in range(32):
            if (mask >> i) & 1:
                cnt += 1
        return cnt

    def dp(self, A, mask, dp):
        mod = 10 ** 9 + 7
        row = self.cnt_bits(mask)
        if row == len(A):
            return 1

        if (row, mask) in dp:
            return dp[(row, mask)]

        ans = 0
        for col in range(len(A[row])):
            if (mask >> col) & 1 == 0 and A[row][col] == 1:
                ans += self.dp(A, mask | (1 << col), dp)

        ans %= mod
        dp[(row, mask)] = ans
        return ans

    def solve(self, A):
        dp = {}
        return self.dp(A, 0, dp)

if __name__ == '__main__':
    A = [[0, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]

    B = Solution()
    print(B.solve(A))

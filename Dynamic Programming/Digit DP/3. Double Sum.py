class Solution:
    def dp(self, A, pos, flag, digit_sum, dp):
        if pos == len(A):
            return digit_sum

        if (pos, flag, digit_sum) in dp:
            return dp[(pos, flag, digit_sum)]

        lim = 9 if flag else A[pos]
        ans = 0
        for i in range(lim+1):
            ans += self.dp(A, pos+1, 1 if i < A[pos] else flag, digit_sum + i, dp)

        dp[(pos, flag, digit_sum)] = ans
        return ans


    def solve(self, A):
        mod = 10 ** 9 + 7
        n = len(A)
        ans = []
        for i in range(n//2):
            dp = {}
            l = str(int(A[2 * i]) - 1)
            l = [int(i) for i in l]

            r = A[2 * i + 1]
            r = [int(i) for i in r]

            h = self.dp(l, 0, 0, 0, dp)
            dp.clear()
            k = self.dp(r, 0, 0, 0, dp)
            ans.append((k-h)%mod)

        return ans


if __name__ == '__main__':
    A = ["1", "5", "22", "23"]
    B = Solution()
    print(B.solve(A))

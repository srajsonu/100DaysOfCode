class Solution:
    def dp(self, A, B, pos, lflag, rflag, non_zero, dp):
        if pos == len(A) or pos == len(B):
            return non_zero == 3

        lLimit = 0 if lflag else A[pos]
        rLimit = 9 if rflag else B[pos]
        ans = 0

        for i in range(lLimit, rLimit+1):
            if i != 0 and non_zero == 3:
                continue

            ans += self.dp(A, B, pos+1,
                           1 if i > A[pos] else lflag,
                           1 if i < B[pos] else rflag,
                           non_zero + 1 if i != 0 else non_zero, dp)
        print(lLimit, rLimit, ans)
        return ans

    def solve(self, A):
        mod = 10 ** 9 + 7
        n = len(A)
        ans = []
        for i in range(n // 2):
            dp = {}

            start = str(int(A[2 * i]))
            start = [int(i) for i in start]

            end = A[2 * i + 1]
            end = [int(i) for i in end]

            h = self.dp(start, end, 0, 0, 0, 0, dp)
            ans.append(h % mod)

        return ans

if __name__ == '__main__':
    A = ['1', '40']
    B = Solution()
    print(B.solve(A))

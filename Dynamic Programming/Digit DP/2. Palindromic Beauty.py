class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def dp(self, A, pos, flag, curr, dp):
        if pos == len(A):
            return 0

        lim = 9 if flag else A[pos]
        ans = 0

        for i in range(lim+1):
            if not self.isPalindrome(str(curr)):
                continue

            ans += self.dp(A, pos+1, 1 if i < A[pos] else flag, curr+i, dp)

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

            h = self.dp(l, 0, 0, 0, 0, dp)
            dp.clear()
            k = self.dp(r, 0, 0, 0, 0, dp)
            print(h, k)


        return ans


if __name__ == '__main__':
    A = ["1", "10"]
    B = Solution()
    print(B.solve(A))

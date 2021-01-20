import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def dp(self, s, i, j, isTrue, dp):
        if i > j:
            return 1

        if i == j:
            if isTrue:
                return 1 if s[i] == 'T' else 0
            else:
                return 1 if s[i] == 'F' else 0

        if (i, j, isTrue) in dp:
            return dp[(i, j, isTrue)]

        ans = 0
        for k in range(i+1, j, 2):
            lt = self.dp(s, i, k-1, True, dp)
            lf = self.dp(s, i, k-1, False, dp)
            rt = self.dp(s, k+1, j, True, dp)
            rf = self.dp(s, k+1, j, False,dp)
            if s[k] == '&':
                if isTrue:
                    ans += lt * rt
                else:
                    ans += lt * rf + lf * rt + lf * rf

            elif s[k] == '^':
                if isTrue:
                    ans += lt * rf + lf * rt
                else:
                    ans += lf * rf + lt * rt

            else:
                if isTrue:
                    ans += lt * rt + lf * rt + lt * rf
                else:
                    ans += lf * rf

        ans %= 1003
        dp[(i, j, isTrue)] = ans
        return ans

    def cnttrue(self, s):
        n = len(s)
        dp = {}
        return self.dp(s, 0, n-1, True, dp)

if __name__ == '__main__':
    A = "T^T^T^F|F"
    B = Solution()
    print(B.cnttrue(A))

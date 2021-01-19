import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def dp(self, s, dp):
        n = len(s)
        if not s:
            return 0

        if self.isPalindrome(s):
            return 0

        if s in dp:
            return dp[s]

        ans = float('inf')
        for i in range(1, n+1):
            if self.isPalindrome(s[0:i]):
                ans = min(ans, 1 + self.dp(s[i:n], dp))

        dp[s] = ans
        return ans

    def minCut(self, s):
        self.ans = float('inf')
        dp = {}
        return self.dp(s, dp)

if __name__ == '__main__':
    A = "dVGAaVO25EmT6W3zSTEA0k12i64Kkmmli09Kb4fArlF4Gc2PknrlkevhROxUg"
    B = Solution()
    print(B.minCut(A))

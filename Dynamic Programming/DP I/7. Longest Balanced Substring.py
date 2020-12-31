class Solution:
    def solve(self, s):
        n = len(s)
        dp = [0 for _ in range(n)]
        if n <= 1: return 0
        ans = float('-inf')
        for i in range(1, n):
            if (s[i] == ')' and s[i-1] == '(') or (s[i] == '}' and s[i-1] == '{') or (s[i] == ']' and s[i-1] == '['):
                dp[i] = dp[i-2] + 2

            if (s[i] == ')' or s[i] == '}' or s[i] == ']' ) and (s[i-1] == ')' or s[i-1] == ']' or s[i-1] == '}'):
                if (s[i - dp[i-1] - 1] == '(' and s[i] == ')') or (s[i - dp[i-1] - 1] == '{' and s[i] == '}') or (s[i - dp[i-1] - 1] == '[' and s[i] == ']'):
                    dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]

            ans = max(ans, dp[i])

        return ans


if __name__ == '__main__':
    s = '([[]]()}['
    t = Solution()
    print(t.solve(s))

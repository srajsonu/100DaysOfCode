import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def dp(self, s, dic, dp):
        if not s:
            return 1

        if s in dic:
            return 1

        if s in dp:
            return dp[s]

        for i in range(1, len(s) + 1):
            if s[0:i] in dic and self.dp(s[i:len(s)], dic, dp):
                dp[s] = 1
                return dp[s]

        dp[s] = 0
        return dp[s]

    def wordBreak(self, s, dic):
        dp = {}
        return self.dp(s, dic, dp)

    def solve(self, s, dic):
        n = len(s)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            if s[0:i] in dic and not dp[i]:
                dp[i] = 1

            if dp[i]:
                if i == n: return True
                for j in range(i+1, n+1):
                    if not dp[j] and s[i:j] in dic:
                        dp[j] = 1

                    if j == n and dp[j]:
                        return 1

        return 0


if __name__ == '__main__':
    s = 'ilikemangoes'
    dic = {'i', 'like', 'man', 'go', 'mangoes'}
    t = Solution()
    print(t.wordBreak(s, dic))
    print(t.solve(s, dic))

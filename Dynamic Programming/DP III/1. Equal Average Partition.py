class Solution:
    def dp(self, A, i, s1, cnt, res, dp):#sm = 12, cnt = 1
        global ans
        key = str(i) + str(s1) + str(cnt)
        if key in dp:
            return dp[key] == True

        if cnt == 0:
            return s1 == 0

        if i >= len(A): return False

        if A[i] <= s1:
            res.append(A[i])
            if self.dp(A, i+1, s1 - A[i], cnt-1, res, dp):
                dp[key] = True
                return dp[key]
            res.pop()

        if self.dp(A, i+1, s1, cnt, res, dp):
            dp[key] = True
            return dp[key]

        dp[key] = False
        return False


    def solve(self, A):
        n = len(A)
        S = sum(A)
        dp = {}
        for i in range(1, n-1):
            if (S * i) % n == 0:
                s1 = (S * i) // n
                res = []
                if self.dp(A, 0, s1, i, res, dp):
                    tmp = res[:]
                    return [res, [i for i in A if not i in tmp or tmp.remove(i)]]

        return []

if __name__ == '__main__':
    A = [1, 7, 15, 29, 11, 9]
    B = Solution()
    print(B.solve(A))

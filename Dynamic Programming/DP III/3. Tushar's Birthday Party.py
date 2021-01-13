class Solution:
    def dp(self,A, B, C, i, dp):
        global ans
        if i == len(B) or A < 0:
            return float('inf')

        if A == 0: return 0
        if (A, i) in dp: return dp[(A, i)]

        if A - B[i] >= 0:
            take = self.dp(A - B[i], B, C, i, dp) + C[i]
            dont = self.dp(A, B, C, i+1, dp)
            ans = min(take, dont)
        else:
            ans = self.dp(A, B, C, i+1, dp)

        dp[(A, i)] = ans
        return ans

    def solve(self, A, B, C):
        dp = {}
        ans = 0
        for i in A:
            val = self.dp(i, B, C, 0, dp)
            ans += val
        return ans

if __name__ == '__main__':
    A = [2, 4, 6]
    B = [2, 1, 3]
    C = [2, 5, 3]
    D = Solution()
    print(D.solve(A, B, C))

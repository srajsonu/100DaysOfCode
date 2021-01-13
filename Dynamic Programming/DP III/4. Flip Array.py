class Solution:
    def dp(self, A, i, sm, dp):
        global ans
        if sm == 0:
            return 0
        if (i, sm) in dp:
            return dp[(i, sm)]
        if i == len(A):
            ans = float('inf')
        else:
            take = self.dp(A, i + 1, sm - A[i] * 2, dp) + 1
            dont = self.dp(A, i + 1, sm, dp)
            ans = min(take, dont)
        print(sm, ans)
        dp[(i, sm)] = ans
        return ans

    def solve(self, A):
        dp = {}
        sm = sum(A)
        return self.dp(A, 0, sm, dp)


if __name__ == '__main__':
    A = [8, 4, 5, 7, 6, 2]
    B = Solution()
    print(B.solve(A))

class Solution:
    def dp(self, A, i, res, dp):#Done by Bit-masking dp
        global ans
        if i == len(A):
            return 0
        else:
            take = self.dp(A, i, res + A[i], dp)
            dont = self.dp(A, i+1, res, dp)
            ans = min()

    def solve(self, A):
        n = len(A)
        dp = [0 for _ in  range(n+1)]
        return self.dp(A, 1, [],dp)

if __name__ == '__main__':
    A = [1, 2, 4, 3]
    B = Solution()
    print(B.solve(A))

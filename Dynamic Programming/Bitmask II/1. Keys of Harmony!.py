class Solution:
    def dp(self, A, row, mask, ans, dp):
        if row == len(A):
            return 0

        if (row, mask) in dp:
            return dp[(row, mask)]

        dp[(row, mask)] = self.dp(A, row+1, mask, ans, dp)

        for col in range(1, 2*A[row]):
            pMask = 0
            for j in range(len(self.prime)):
                if A[col] % self.prime[j] == 0:
                    pMask |= (1 << j)

            if not (mask & pMask):
                pass



    def solve(self, A, n):
        m = 51
        sieve = [0 for _ in range(m)]
        self.prime = []

        for i in range(2, m):
            if not sieve[i]:
                self.prime.append(i)
                for j in range(i * i, m, i):
                    sieve[j] = 1



if __name__ == '__main__':
    S = Solution()
    n = 5
    arr = [1, 6, 4, 2, 8]
    print(S.solve(arr, n))

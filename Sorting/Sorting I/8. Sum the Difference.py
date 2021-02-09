class Solution:
    def solve(self, A):
        A.sort()
        n = len(A)
        mn = 0
        mx = 0

        for i in range(n):
            mx += (2 ** i) * A[i]

        for i in range(n):
            mn += ((2 ** (n-i-1)) * A[i])

        return mx - mn

if __name__ == '__main__':
    A = [1, 3, 2, 5, 7]
    B = Solution()
    print(B.solve(A))

class Solution:
    def solve(self, A):
        n = len(A)
        l = [1 for _ in range(n)]
        r = [1 for _ in range(n)]

        for i in range(1, n):
            if A[i] > A[i-1]:
                l[i] += l[i-1]

        for i in reversed(range(n-1)):
            if A[i] > A[i+1]:
                r[i] += r[i-1]

        ans = 0
        for i in range(n):
            ans += max(l[i], r[i])

        return ans

if __name__ == '__main__':
    A = [3, 1, 2, 2]
    B = Solution()
    print(B.solve(A))

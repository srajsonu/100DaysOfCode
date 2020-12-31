class Solution:
    def solve(self, A):
        if not A: return 0
        n = len(A)
        mn = [0 for _ in range(n)]
        mx = [0 for _ in range(n)]
        mn[0] = A[0]
        mx[0] = A[0]
        ans = A[0]
        for i in range(1, n):
            mn[i] = min(A[i], A[i] * mn[i-1], A[i] * mx[i-1])
            mx[i] = max(A[i], A[i] * mn[i - 1], A[i] * mx[i - 1])
            ans = max(ans, mx[i], mn[i])

        return ans


if __name__ == '__main__':
    A = [-1, 2, 4, -5]
    B = Solution()
    print(B.solve(A))

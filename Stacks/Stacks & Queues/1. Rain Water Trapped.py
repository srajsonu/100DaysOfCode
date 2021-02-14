class Solution:
    def trap(self, A):
        n = len(A)
        l = [0 for _ in range(n)]
        l[0] = A[0]
        for i in range(1, n):
            l[i] = max(l[i-1], A[i])

        r = [0 for _ in range(n)]
        r[n-1] = A[n-1]
        for i in reversed(range(n-1)):
            r[i] = max(r[i+1], A[i])

        ans = 0
        for i in range(n):
            ans += min(l[i], r[i]) - A[i]

        return ans

if __name__ == '__main__':
    A = [0, 1, 0, 2]
    B = Solution()
    print(B.trap(A))

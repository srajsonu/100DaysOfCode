class Solution:
    def solve(self, A):
        n = len(A)
        mn = min(A)
        mx = max(A)

        freq = [0 for _ in range(mn, mx+1)]

        for i in A:
            freq[i] += 1

        for i in range(1, len(freq)):
            freq[i] += freq[i-1]

        ans = [0 for _ in range(n)]

        for i in range(n-1, -1, -1):
            ans[freq[A[i]]-1] = A[i]
            freq[A[i]] -= 1

        return ans


if __name__ == '__main__':
    A = [1, 5, 0, 6, 1, 2, 3, 4, 0, 1]
    B = Solution()
    print(B.solve(A))

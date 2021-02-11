class Solution:
    def solve(self, A):
        n = len(A)
        freq = {}
        ans = 0

        for i in range(n):
            if A[i] not in freq:
                freq[A[i]] = 1

        for i in range(n-1):
            for j in range(i+1, n):
                sm = A[i] + A[j]
                if sm in freq:
                    ans += 1

        return ans

if __name__ == '__main__':
    A = [14, 13, 1, 7, 11, 3, 9, 6, 15, 2, 12, 8, 4, 10, 5 ]
    B = Solution()
    print(B.solve(A))

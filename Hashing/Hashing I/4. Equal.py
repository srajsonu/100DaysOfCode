class Solution:
    def equal(self, A):
        n = len(A)
        freq = {}

        for i in range(n-1):
            for j in range(1, n):
                sm = A[i] + A[j]
                if sm not in freq:
                    freq[sm] = [i, j]

        ans = []
        for i in range(n-1):
            for j in range(i+1, n):
                sm = A[i] + A[j]
                i1, j1 = freq[sm]
                if sm in freq and (i != i1 and j != i1 and j != j1 and i != j1 and i1 != j1):
                    curr = [i1, j1, i, j]
                    if not ans or ans > curr:
                        ans = curr

        return ans

if __name__ == '__main__':
    A = [3, 4, 7, 1, 2, 9, 8]
    B = Solution()
    print(B.equal(A))

class Solution:
    def solve(self, A):
        n = len(A)
        for i in range(n):
            for j in range(n-i-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
        return A

if __name__ == '__main__':
    A = [3, 5, 9, 6, 2, 4]
    B = Solution()
    print(B.solve(A))

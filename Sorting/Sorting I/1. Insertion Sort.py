class Solution:
    def solve(self, A):
        n = len(A)
        for i in range(1, n):
            key = A[i]
            j = i-1
            while j >= 0 and A[j] > key:
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key

        return A

if __name__ == '__main__':
    A = [3, 5, 9, 6, 2, 4]
    B = Solution()
    print(B.solve(A))

class Solution:
    def searchMatrix(self, A, B):
        m = len(A)
        n = len(A[0])
        i = 0
        j = n-1

        while i <= m-1 and j >= 0:
            if A[i][j] == B:
                return 1

            if A[i][-1] < B:
                i += 1
            else:
                j -= 1

        return 0


if __name__ == '__main__':
    A = [[1, 3, 5, 7],
         [10, 11, 16, 20],
         [23, 30, 34, 50]]
    B = 3
    C = Solution()
    print(C.searchMatrix(A, B))

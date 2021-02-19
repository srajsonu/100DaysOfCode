class Solution:
    def solve(self, A):
        m = len(A)
        n = len(A[0])
        for k in range(n):
            for i in range(m):
                for j in range(n):
                    if A[i][j] == -1:
                        A[i][j] = float('inf')

                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])

        for i in range(m):
            for j in range(n):
                if A[i][j] == float('inf'):
                    A[i][j] = -1

        return A

if __name__ == '__main__':
    A = [[0, 50, 39],
         [-1, 0, 1],
         [-1, 10, 0]]
    B = Solution()
    print(B.solve(A))

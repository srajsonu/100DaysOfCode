class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def dfs(self, A, i, j, vis):
        vis.add((i, j))

        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c

            if self.isValid(A, nRow, nCol) and (nRow, nCol) not in vis and A[nRow][nCol] == 'O':
                vis.add((nRow, nCol))
                self.dfs(A, nRow, nCol, vis)

    def solve(self, A):
        m = len(A)
        n = len(A[0])
        vis = set()
        for i in range(m):
            if A[i][0] == 'O':
                self.dfs(A, i, 0, vis)

            if A[i][n-1] == 'O':
                self.dfs(A, i, n-1, vis)

        for j in range(n):
            if A[0][j] == 'O':
                self.dfs(A, 0, j, vis)

            if A[m-1][j] == 'O':
                self.dfs(A, m-1, j, vis)

        for i in range(m):
            for j in range(n):
                if (i, j) not in vis:
                    if A[i][j] == 'O':
                        A[i][j] = 'X'


        return A


if __name__ == '__main__':
    A = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]
    B = Solution()
    print(B.solve(A))

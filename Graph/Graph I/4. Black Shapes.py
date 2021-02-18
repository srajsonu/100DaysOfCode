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

            if self.isValid(A, nRow, nCol) and (nRow, nCol) not in vis and A[nRow][nCol] == 'X':
                vis.add((nRow, nCol))
                self.dfs(A, nRow, nCol, vis)

    def black(self, A):
        m = len(A)
        n = len(A[0])
        vis = set()
        ans = 0

        for i in range(m):
            for j in range(n):
                if A[i][j] == 'X' and (i, j) not in vis:
                    self.dfs(A, i, j, vis)
                    ans += 1

        return ans



if __name__ == '__main__':
    A = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['O', 'X', 'O', 'O'],
         ['X', 'O', 'X', 'X']]
    B = Solution()
    print(B.black(A))

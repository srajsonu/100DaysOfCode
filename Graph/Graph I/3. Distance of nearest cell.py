from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def solve(self, A):
        m = len(A)
        n = len(A[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    q.append((i, j))
                    A[i][j] = 0
                else:
                    A[i][j] = -1

        row = [0, -1, 0, 1]
        col = [-1, 0, 1, 0]
        vis = set()
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                vis.add((i, j))
                for r, c in zip(row, col):
                    nRow = i + r
                    nCol = j + c

                    if self.isValid(A, nRow, nCol) and A[nRow][nCol] != A[i][j] and (nRow, nCol) not in vis:
                        A[nRow][nCol] = A[i][j] + 1
                        q.append((nRow, nCol))
                        vis.add((nRow, nCol))

        return A



if __name__ == '__main__':
    A = [[0, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 1, 1, 0]]
    B = Solution()
    print(B.solve(A))

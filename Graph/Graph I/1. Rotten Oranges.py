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
        vis = set()

        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]
        for i in range(m):
            for j in range(n):
                if A[i][j] == 2:
                    q.append((i, j, 0))
                    # break
        ans = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y, ans = q.popleft()
                vis.add((x, y))

                for r, c in zip(row, col):
                    nRow = x + r
                    nCol = y + c

                    if self.isValid(A, nRow, nCol) and A[nRow][nCol] == 1 and (nRow, nCol) not in vis:
                        A[nRow][nCol] = 2
                        vis.add((nRow, nCol))
                        q.append((nRow, nCol, ans + 1))

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    return -1

        return ans


if __name__ == '__main__':
    A = [[2, 1, 1],
         [1, 1, 0],
         [0, 1, 1]]
    B = Solution()
    print(B.solve(A))

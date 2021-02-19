from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def solve(self, A, B, C):
        m = len(A)
        n = len(A[0])
        q = deque()
        q.append((B[0], B[1]))
        vis = set()
        dis = [[float('inf') for _ in range(n)] for _ in range(m)]
        dis[B[0]][B[1]] = 0
        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        while q:
            i, j = q.popleft()
            vis.add((i, j))
            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c
                count = 0
                while self.isValid(A, nRow, nCol) and A[nRow][nCol] == 0:
                    nRow += r
                    nCol += c
                    count += 1

                if dis[i][j] + count < dis[nRow-r][nCol-c] and (nRow-r, nCol-c) not in vis:
                    dis[nRow-r][nCol-c] = dis[i][j] + count
                    vis.add((nRow-r, nCol-c))
                    q.append((nRow-r, nCol-c))

        return dis[C[0]][C[1]] if dis[C[0]][C[1]] != float('inf') else -1


if __name__ == '__main__':
    A = [[0, 0], [0, 0]]
    B = [0, 0]
    C = [0, 1]
    D = Solution()
    print(D.solve(A, B, C))

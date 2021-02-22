from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] == '1':
            return False
        return True

    def solve(self, A, B, C, D, E):
        m = len(E)
        n = len(E[0])

        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        q = deque()
        q.append((A-1, B-1, 0))
        vis = set()
        while q:
            i, j, k = q.popleft()
            vis.add((i, j))

            if i == C-1 and j == D-1:
                return k

            # for r, c in zip(row, col):
            #     nRow = i + r
            #     nCol = j + c
            #     if self.isValid(E, nRow, nCol) and (nRow, nCol) not  in vis:
            #         vis.add((nRow, nCol))
            #         q.append((nRow, nCol, k+1))


            for x in range(i-1, -1, -1):
                if E[x][j] == '0' and (x, j) not in vis:
                    vis.add((x, j))
                    q.append((x, j, k+1))
                else:
                    break

            for y in range(j-1, -1, -1):
                if E[i][y] == '0' and (i, y) not in vis:
                    vis.add((i, y))
                    q.append((i, y, k+1))
                else:
                    break

            for x in range(i+1, m):
                if E[x][j] == '0' and (x, j) not in vis:
                    vis.add((x, j))
                    q.append((x, j, k+1))
                else:
                    break

            for y in range(j+1, n):
                if E[i][y] == '0' and (i, y) not in vis:
                    vis.add((i, y))
                    q.append((i, y, k+1))
                else:
                    break

        return -1



if __name__ == '__main__':
    A = 1
    B = 1
    C = 3
    D = 6
    E = [ "0000000000",
          "0111111110",
          "0000100010",
          "0000100000",
          "0000000010",
          "0000100100",
          "0000100010",
          "0000100100",
          "0010001010",
          "1000101000" ]
    F = Solution()
    print(F.solve(A, B, C, D, E))

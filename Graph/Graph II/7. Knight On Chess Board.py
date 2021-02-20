from collections import deque


class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def knight(self, A, B, C, D, E, F):
        if E > A or F > B: return -1
        graph = [[-1 for _ in range(B)] for _ in range(A)]
        q = deque()
        q.append((C - 1, D - 1, 0))
        graph[C - 1][D - 1] = 0
        row = [-1, 1, -2, 2, -2, 2, -1, 1]
        col = [-2, -2, -1, -1, 1, 1, 2, 2]
        while q:
            i, j, k = q.popleft()
            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c
                if self.isValid(graph, nRow, nCol) and graph[nRow][nCol] == -1:
                    graph[nRow][nCol] = k + 1
                    q.append((nRow, nCol, k + 1))

        return graph[E - 1][F - 1]


if __name__ == '__main__':
    A = 8
    B = 8
    C = 1
    D = 1
    E = 8
    F = 8
    G = Solution()
    print(G.knight(A, B, C, D, E, F))

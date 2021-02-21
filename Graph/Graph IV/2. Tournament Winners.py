class Solution:
    def solve(self, A, B):
        m = len(B)
        n = len(B[0])

        for i in range(m):
            for j in range(n):
                pass




if __name__ == '__main__':
    A = 4
    B = [[0, 1, 1, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]
    C = Solution()
    print(C.solve(A, B))

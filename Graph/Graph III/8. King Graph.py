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

        global ans
        max_min_dis = float('inf')
        for i in range(m):
            max_dis = float('-inf')
            for j in range(n):
                max_dis = max(max_dis, A[i][j])

            if max_min_dis > max_dis:
                max_min_dis = max_dis
                ans = i

        return ans

if __name__ == '__main__':
    A = [[0, 6, 8, -1],
         [6, 0, 9, -1],
         [8, 9, 0, 4],
         [-1, -1, 4, 0]]
    B = Solution()
    print(B.solve(A))

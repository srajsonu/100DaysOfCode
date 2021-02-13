class Solution:
    def histogram(self, A):
        A += [0]
        n = len(A)
        stack = [-1]
        ans = 0

        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                tmp = stack.pop()
                area = (i - stack[-1] - 1) * A[tmp]
                ans = max(area, ans)

            stack.append(i)

        return ans

    def solve(self, A):
        m = len(A)
        n = len(A[0])
        for i in range(1, m):
            for j in range(n):
                if A[i][j] == 0:
                    continue
                A[i][j] += A[i - 1][j]

        ans = 0
        for i in A:
            area = self.histogram(i)
            ans = max(area, ans)

        return ans


if __name__ == '__main__':
    A = [[0, 0, 1],
         [0, 1, 1],
         [1, 1, 1]]

    B = Solution()
    print(B.solve(A))

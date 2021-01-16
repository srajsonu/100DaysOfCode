from collections import deque


class Solution:
    def histogram(self, A):
        n = len(A)
        stack = deque()
        i = 0
        max_area = 0

        while i < n:
            if not stack or A[stack[-1]] <= A[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                area = A[top] * ((i - stack[-1] - 1) if stack else i)
                max_area = max(area, max_area)

        while stack:
            top = stack.pop()
            area = A[top] * ((i - stack[-1] - 1) if stack else i)
            max_area = max(area, max_area)

        return max_area

    def maximalRectangle(self, A):
        m = len(A)
        n = len(A[0])

        for i in range(m):
            for j in range(1, n):
                if A[j][i] == 0:
                    continue
                A[j][i] += A[j-1][i]
        ans = 0
        for i in A:
            area = self.histogram(i)
            ans = max(area, ans)

        return ans


if __name__ == '__main__':
    A = [[1, 1, 1],
         [0, 1, 1],
         [1, 0, 0]]

    B = Solution()
    print(B.maximalRectangle(A))

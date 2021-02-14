class Solution:
    def largestRectangleArea(self, A):
        n = len(A)
        if n == 1:
            return A[0]
        l = [-1 for _ in range(n)]
        r = [n for _ in range(n)]
        stack = []
        for i in range(n):
            while stack:
                tmp = stack.pop()
                if A[i] < A[tmp]:
                    r[tmp] = i
                else:
                    stack.append(tmp)
                    break

            stack.append(i)

        stack.clear()
        for i in reversed(range(n)):
            while stack:
                tmp = stack.pop()
                if A[i] < A[tmp]:
                    l[tmp] = i
                else:
                    stack.append(tmp)
                    break

            stack.append(i)

        ans = 0
        for i in range(n):
            area = (r[i] - l[i] - 1) * A[i]
            ans = max(area, ans)

        return ans

    def solve(self, A):
        A.append(0)
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

if __name__ == '__main__':
    A = [90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]
    B = Solution()
    print(B.largestRectangleArea(A))
    print(B.solve(A))

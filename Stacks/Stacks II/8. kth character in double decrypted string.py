class Solution:
    def solve(self, A, B):
        n = len(A)
        stack = []
        cnt = 0
        num = ""
        for i in range(n):
            if A[i].isnumeric():
                num += A[i]
            else:
                if num:
                    cnt *= int(num)
                num = ""
                cnt += 1
                stack.append((A[i], cnt))
        k = 0

        while stack:
            i, j = stack.pop()
            k = j % B

        return A[k-1]

if __name__ == '__main__':
    A = "x2y3"
    B = 3
    C = Solution()
    print(C.solve(A, B))

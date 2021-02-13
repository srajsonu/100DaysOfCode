class Solution:
    def braces(self, A):
        n = len(A)
        stack = []

        for i in A:
            while stack:
                pass

            stack.append(i)


if __name__ == '__main__':
    A = "((a+b))"
    B = Solution()
    print(B.braces(A))

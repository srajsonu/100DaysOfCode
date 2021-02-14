class Solution:
    def prevSmaller(self, A):
        n = len(A)
        stack = []
        ans = [-1 for _ in range(n)]
        for i in reversed(range(n)):
            while stack:
                tmp = stack.pop()
                if A[tmp] > A[i]:
                    ans[tmp] = A[i]
                else:
                    stack.append(tmp)
                    break

            stack.append(i)

        return ans

if __name__ == '__main__':
    A = [4, 5, 2, 10, 8]
    B = Solution()
    print(B.prevSmaller(A))

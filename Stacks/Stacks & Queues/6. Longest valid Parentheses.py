class Solution:
    def longestValidParentheses(self, A):
        n = len(A)
        stack = [-1]
        ans = 0
        for i in range(n):
            if A[i] == ')':
                stack.pop()
                if stack:
                    ans = max(ans, i - stack[-1])
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return ans


if __name__ == '__main__':
    A = ")()())"
    B = Solution()
    print(B.longestValidParentheses(A))

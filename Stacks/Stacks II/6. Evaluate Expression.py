from math import floor


class Solution:
    def evalRPN(self, A):
        n = len(A)
        stack = []
        for i in range(n):
            if A[i] == '+' or A[i] == '-' or A[i] == '*' or A[i] == '/':
                while stack:
                    a = stack.pop()
                    b = stack.pop()
                    if A[i] == '+':
                        val = b + a
                        stack.append(val)
                        break
                    elif A[i] == '-':
                        val = b - a
                        stack.append(val)
                        break
                    elif A[i] == '*':
                        val = b * a
                        stack.append(val)
                        break
                    else:
                        val = floor(b / a)
                        stack.append(val)
                        break
            else:
                stack.append(int(A[i]))

        return stack[0]


if __name__ == '__main__':
    A = ["4", "13", "5", "/", "+"]
    B = Solution()
    print(B.evalRPN(A))

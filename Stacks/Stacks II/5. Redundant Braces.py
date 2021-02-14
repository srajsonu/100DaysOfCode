class Solution:
    def braces(self, A):
        stack = []
        for i in A:
            if i.isalpha():
                continue
            if i == ')':
                top = stack.pop()
                flag = True
                while top != '(':
                    if top == '+' or top == '-' or top == '*' or top == '/':
                        flag = False
                    top = stack.pop()

                if flag:
                    return 1

            stack.append(i)

        return 0


if __name__ == '__main__':
    A = "(a+(a+b))"
    B = Solution()
    print(B.braces(A))

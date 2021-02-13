class Solution:
    def solve(self, A):
        stack = []

        while A:
            tmp = A.pop()
            while stack:
                val = stack.pop()
                if val > tmp:
                    A.append(val)
                else:
                    stack.append(val)
                    break

            stack.append(tmp)

        return stack

if __name__ == '__main__':
    A = [5, 17, 100, 11]
    B = Solution()
    print(B.solve(A))

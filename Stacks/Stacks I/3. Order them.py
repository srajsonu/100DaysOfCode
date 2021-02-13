class Solution:
    def solve(self, A):
        B = []
        C = []

        while A:
            tmp = A.pop(0)
            while B:
                val = B.pop()
                if val <= tmp:
                    while C:
                        val2 = C.pop()
                        if val2 > val:
                            return 0
                        else:
                            C.append(val2)
                            break
                    C.append(val)
                else:
                    B.append(val)
                    break

            B.append(tmp)

        while B:
            tmp = B.pop()
            while C:
                val = C.pop()
                if val > tmp:
                    return 0
                else:
                    C.append(val)
                    break

            C.append(tmp)

        return 1


if __name__ == '__main__':
    A = [5, 3, 1, 4, 2]
    B = Solution()
    print(B.solve(A))

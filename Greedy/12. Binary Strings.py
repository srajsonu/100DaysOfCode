class Solution:
    def solve(self, A, B):
        A = [i for i in A]
        n = len(A)
        ans = 0

        for i in range(n):
            if A[i] == '0':
                if i + B - 1 < n:
                    for j in range(i, i+B):
                        if A[j] == '0':
                            A[j] = '1'
                        else:
                            A[j] = '0'

                    ans += 1
                else:
                    break

        for i in A:
            if i == '0':
                return -1

        return ans


if __name__ == '__main__':
    A = "00010110"
    B = 3
    C = Solution()
    print(C.solve(A))

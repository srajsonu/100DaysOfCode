from math import gcd


class Solution:
    def solve(self, A):
        A.sort()
        n = len(A)

        if n > 2:
            for i in range(2, n):
                if A[i] != A[i-1] + gcd(A[i-1], A[i-2]):
                    return [-1]
            return A
        else:
            if n == 2:
                if A[0] < A[1]:
                    return A
                else:
                    A[0], A[1] = A[1], A[0]
                    return A
            else:
                return A

if __name__ == '__main__':
    A = [4, 6, 2, 5, 3]
    B = Solution()
    print(B.solve(A))

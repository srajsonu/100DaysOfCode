class Solution:
    def solve(self, A, B, C):
        i = len(A) - 1
        j = len(B) - 1
        k = len(C) - 1

        ans = float('inf')
        while i >= 0 and j >= 0 and k >= 0:
            a = A[i]
            b = B[j]
            c = C[k]

            ans = min(ans, abs(max(a, b, c) - min(a, b, c)))

            if a >= b and a >= c:
                i -= 1
            elif b >= a and b >= c:
                j -= 1
            else:
                k -= 1

        return ans

if __name__ == '__main__':
    A = [1, 4, 5, 8, 10]
    B = [6, 9, 15]
    C = [2, 3, 6, 6]
    D = Solution()
    print(D.solve(A, B, C))

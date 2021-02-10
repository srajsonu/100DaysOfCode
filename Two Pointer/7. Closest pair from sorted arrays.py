class Solution:
    def solve(self, A, B, C):
        m = len(A)
        n = len(B)

        i = 0
        j = n - 1
        diff = float('inf')
        ans = [-1, -1]
        ind = [-1, -1]
        while i <= m - 1 and j >= 0:
            tmp = abs(A[i] + B[j] - C)
            if diff > tmp:
                diff = tmp
                ans = [A[i], B[j]]
                ind = [i, j]

            elif diff == tmp:
                if i == ind[0]:
                    ans = [A[i], B[j]]
                    ind[1] = j

            if A[i] + B[j] >= C:
                j -= 1
            else:
                i += 1

        return ans


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = [2, 4, 6, 8]
    C = 9
    D = Solution()
    print(D.solve(A, B, C))

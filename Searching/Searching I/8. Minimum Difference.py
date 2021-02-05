class Solution:
    def findUpper(self, A, B):
        n = len(A)
        l = 0
        h = n-1
        while l <= h:
            mid = (l + h) // 2

            if A[mid] < B:
                l = mid + 1
            else:
                h = mid - 1

        return l - 1

    def findLower(self, A, B):
        n = len(A)
        l = 0
        h = n-1
        while l <= h:
            mid = (l + h) // 2
            if A[mid] <= B:
                l = mid + 1
            else:
                h = mid - 1

        return l - 1

    def solve(self, A, B, C):
        for i in range(A):
            C[i] = sorted(C[i])

        ans = 0
        for i in range(A-1):
            for j in range(B):
                upper = self.findUpper(C[i+1], C[i][j])
                lower = self.findLower(C[i+1], C[i][j])
                ans = min(ans, min(C[i+1][upper] - C[i][j], C[i][j] - C[i+1][lower]))

        return ans


if __name__ == '__main__':
    A = 3
    B = 2
    C = [[7, 3],
         [2, 1],
         [4, 9]]
    D = Solution()
    print(D.solve(A, B, C))

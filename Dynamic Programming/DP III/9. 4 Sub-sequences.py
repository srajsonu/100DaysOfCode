class Solution:
    def dp(self, A, i, dp):
        if i == len(A):
            return

        take = self.dp(A)
    def solve(self, A):
        pass

if __name__ == '__main__':
    A = [7, 7, 3, 3, 10, 9, 4, 3, 3, 4]
    B = Solution()
    print(B.solve(A))

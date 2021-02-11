class Solution:
    def solve(self, A):
        n = len(A)
        Hash = {}
        sm = 0
        for i in range(n):
            sm += A[i]
            if sm not in Hash:
                Hash[sm] = True
            else:
                return 1

            if sm == 0:
                return 1

        return 0

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = Solution()
    print(B.solve(A))

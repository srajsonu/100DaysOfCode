class Solution:
    def reverse(self, A, i):
        if i == len(A):
            return []
        return self.reverse(A, i+1) + [A[i]]

    def solve(self, A):
        return self.reverse(A, 0)

if __name__ == '__main__':
    A = [1, 5, 3, 2, 4]
    B = Solution()
    print(B.solve(A))

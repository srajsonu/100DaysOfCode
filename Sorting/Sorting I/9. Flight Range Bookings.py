class Solution:
    def solve(self, A, B):
        ans = [0 for _ in range(A)]
        for i, j, k in B:
            ans[i-1] += k
            if j < A:
                ans[j] += -k

        for i in range(1, A):
            ans[i] += ans[i-1]

        return ans

if __name__ == '__main__':
    A = 5
    B = [[1, 2, 10],
         [2, 3, 20],
         [2, 5, 25]]
    C = Solution()
    print(C.solve(A, B))

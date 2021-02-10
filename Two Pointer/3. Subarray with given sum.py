class Solution:
    def solve(self, A, B):
        n = len(A)
        i = 0
        sm = 0
        for j in range(n):
            sm += A[j]
            while sm > B and i <= j:
                sm -= A[i]
                i += 1

            if sm == B:
                ans = []
                for k in range(i, j + 1):
                    ans.append(A[k])
                return ans

        return [-1]

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 5
    C = Solution()
    print(C.solve(A, B))

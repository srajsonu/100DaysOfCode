class Solution:
    def solve(self, A, B):
        mod = 10 ** 9 + 7
        n = len(A)
        i = 0
        j = n - 1
        cnt = 0
        while i <= j:
            if (A[i] * A[j]) < B:
                cnt += 2 * (j - i) + 1
                cnt %= mod
                i += 1
            else:
                j -= 1

        return cnt

if __name__ == '__main__':
    A = [1, 2]
    B = 5
    C = Solution()
    print(C.solve(A, B))

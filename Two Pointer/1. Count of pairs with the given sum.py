class Solution:
    def solve(self, A, B):
        n = len(A)
        i = 0
        j = n - 1
        cnt = 0

        while i < j:
            if (A[i] + A[j]) == B:
                cnt += 1
                i += 1
                j -= 1
            elif (A[i] + A[j]) < B:
                i += 1
            else:
                j -= 1

        return cnt


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 5
    C = Solution()
    print(C.solve(A, B))

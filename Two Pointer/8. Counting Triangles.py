class Solution:
    def solve(self, A):
        A.sort()
        n = len(A)
        cnt = 0
        for i in range(n):
            l = i + 2
            for j in range(i + 1, n):
                sm = A[i] + A[j]
                while l < n and sm > A[l]:
                    cnt += (l-1-j)
                    l += 1

        return cnt


if __name__ == '__main__':
    A = [1, 1, 1, 2, 2]
    B = Solution()
    print(B.solve(A))

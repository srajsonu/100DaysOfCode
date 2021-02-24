class Solution:
    def solve(self, A):
        mod = 10 ** 7 + 3
        n = len(A)
        pos = []
        for i in range(n):
            if A[i] == 'x':
                pos.append(i)

        m = len(pos)
        if m == 0:
            return 0

        mid = m // 2
        cp = pos[mid]

        total_jump = 0
        for i in range(m):
            start = pos[i]
            end = cp - mid + i
            total_jump += abs(start - end)

        return total_jump % mod

if __name__ == '__main__':
    A = "....x..xx...x.."
    B = Solution()
    print(B.solve(A))

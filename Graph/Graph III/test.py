class Solution:
    def solve(self, A):
        A = A.split('=')
        l = [i for i in A[0]]
        r = A[1]
        n = len(r)

        tmp = int("".join(l))
        if tmp == int(r):
            return 0

        if len(l) < len(r):
            return -1

        val = int("".join(l[:n]))
        cnt = 0
        for i in range(n, len(l)):
            val += int(l[i])
            cnt += 1
            if val == int(r):
                return cnt


        return -1


A = '111=12'
B = Solution()
print(B.solve(A))

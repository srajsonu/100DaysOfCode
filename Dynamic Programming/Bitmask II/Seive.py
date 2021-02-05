class Solution:
    def solve(self, A):
        prime = [True for _ in range(A+1)]
        cnt = 0

        p = 2
        while p*p <= A:
            if prime[p]:
                for i in range(p*p, A+1, p):
                    prime[i] = False
            p += 1

        ans = []
        for i in range(2, A+1):
            if prime[i]:
                cnt += 1
                ans.append(i)
            #prime[i] = bin(cnt).replace('0b', '00')

        return prime

    def seive(self, A):
        prime = ["" for _ in range(A+1)]

        for i in range(A):
            pass


if __name__ == '__main__':
    A = 59
    B = Solution()
    print(B.solve(A))

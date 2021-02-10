class Solution:
    def solve(self, A, B, C, D):
        i = 0
        j = 0
        k = 0

        ans = [0 for _ in range(D+1)]
        ans[0] = 1
        for idx in range(1, D+1):
            tmp = min(A*ans[i], B*ans[j], C*ans[k])
            ans[idx] = tmp

            if tmp == A * ans[i]:
                i += 1
            if tmp == B * ans[j]:
                j += 1
            if tmp == C * ans[k]:
                k += 1

        return ans[1:]

if __name__ == '__main__':
    A = 2
    B = 3
    C = 5
    D = 5
    E = Solution()
    print(E.solve(A, B, C, D))

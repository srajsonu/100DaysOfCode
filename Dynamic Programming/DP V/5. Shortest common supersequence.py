import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def lcs(self, A, B, i, j, dp):
        ans = ""
        if i == 0 or j == 0:
            return A[i] if A[i] == B[j] else ""

        if dp[i][j] != "":
            return dp[i][j]

        if A[i] == B[j]:
            ans = A[i] + self.lcs(A, B, i-1, j-1, dp)
        else:
            ans = max(self.lcs(A, B, i-1, j, dp), self.lcs(A, B, i, j-1, dp))

        dp[i][j] = ans
        return ans

    def solve(self, C):
        val = C.split(" ")
        A = val[0]
        B = val[1]
        m = len(A)
        n = len(B)
        dp = [["" for _ in range(n+1)] for _ in range(m+1)]
        lcs = self.lcs(A, B, m-1, n-1, dp)
        ans = ""
        i, j = 0, 0
        for c in lcs[::-1]:
            while A[i] != c:
                ans += A[i]
                i += 1

            while B[j] != c:
                ans += B[j]
                j += 1

            ans += c
            i += 1
            j += 1

        return ans + A[i:] + B[j:]

if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        A = input()
        print(S.solve(A))

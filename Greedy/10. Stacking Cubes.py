class Solution:
    def solve(self, A):
        ans = 0
        for i in range(1, A // 2 + 1):
            if (A - i) % i == 0:
                ans += 1

        return ans

if __name__ == '__main__':
    A = 6
    B = Solution()
    print(B.solve(A))

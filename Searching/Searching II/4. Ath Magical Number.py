from math import gcd


class Solution:
    def solve(self, A, B, C):
        mod = 10 ** 9 + 7
        l = 1
        h = A * max(B, C)
        lcm = (B * C) // gcd(B, C)
        ans = -1
        while l <= h:
            mid = (l + h) // 2
            cnt = (mid // B) + (mid // C) - (mid // lcm)
            if cnt >= A:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1

        return ans % mod

if __name__ == '__main__':
    A = 4
    B = 5
    C = 3
    D = Solution()
    print(D.solve(A, B, C))

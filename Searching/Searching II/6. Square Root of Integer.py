class Solution:
    def sqrt(self, A):
        if A < 2: return A
        l = 1
        h = A // 2
        ans = 0
        while l <= h:
            mid = (l + h) // 2
            if (mid * mid) == A:
                return mid
            elif mid * mid < A:
                l = mid + 1
                ans = mid
            else:
                h = mid - 1

        return ans

if __name__ == '__main__':
    A = 9
    B = Solution()
    print(B.sqrt(A))

class Solution:
    def solve(self, A):
        l = 1
        h = A
        while l <= h:
            mid = (l + h) // 2
            sm = (mid * (mid+1)) // 2
            if sm <= A:
                l = mid + 1
            else:
                h = mid - 1

        return l - 1


if __name__ == '__main__':
    A = 20
    B = Solution()
    print(B.solve(A))

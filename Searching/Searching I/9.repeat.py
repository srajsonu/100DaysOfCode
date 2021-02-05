class Solution:
    def solve(self, A):
        n = len(A)
        l = 0
        h = n-1
        num = 3
        while l <= h:
            mid = (l + h) // 2
            if A[mid] == num and A[mid-1] < num:
                return mid

            if A[mid] >= num:
                h = mid - 1
            else:
                l = mid + 1

        return -1

if __name__ == '__main__':
    A = [0, 0, 1, 2, 3, 3, 4, 5]
    B = Solution()
    print(B.solve(A))

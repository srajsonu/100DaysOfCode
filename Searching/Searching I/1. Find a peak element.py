class Solution:
    def solve(self, A):
        n = len(A)
        l = 0
        h = n-1

        while l <= h:
            mid = (l + h) // 2
            if mid == n-1:
                return A[mid]

            if A[mid-1] < A[mid] and A[mid] > A[mid+1]:
                return A[mid]
            elif A[mid-1] < A[mid] and A[mid] < A[mid+1]:
                l = mid + 1
            elif A[mid-1] > A[mid] and A[mid] > A[mid+1]:
                h = mid-1
            else:
                l = mid + 1

        return -1

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = Solution()
    print(B.solve(A))

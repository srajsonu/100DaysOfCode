class Solution:
    def rotation(self, A, l, h):
        n = len(A)
        mid = (l + h) // 2
        if A[mid] > A[mid+1]:
            return mid

        if A[mid] > A[n-1]:
            return self.rotation(A, mid+1, h)
        else:
            return self.rotation(A, l, mid-1)

    def search(self, A, x):
        n = len(A)
        k = self.rotation(A, 0, n-1) + 1

        l = 0
        h = n-1

        while l <= h:
            mid = (l + h) // 2
            if A[(mid+k)%n] == x:
                return (mid+k)%n
            elif A[(mid+k)%n] < x:
                l = mid + 1
            else:
                h = mid - 1

        return -1

if __name__ == '__main__':
    A = [1, 2]
    B = Solution()
    print(B.search(A, 2))

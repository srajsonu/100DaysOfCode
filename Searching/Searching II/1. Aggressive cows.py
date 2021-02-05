class Solution:
    def place(self, A, B, pos):
        n = len(A)
        place = A[0]
        B -= 1
        for i in range(1, n):
            if not B:
                break
            if A[i] - place >= pos:
                place = A[i]
                B -= 1

        if not B:
            return True
        return False


    def solve(self, A, B):
        l = 1
        h = A[-1]

        while l <= h:
            mid = (l+h) // 2
            if self.place(A, B, mid) and not self.place(A, B, mid+1):
                return mid
            if self.place(A, B, mid):
                l = mid + 1
            else:
                h = mid - 1

        return -1

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 3
    C = Solution()
    print(C.solve(A, B))

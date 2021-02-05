class Solution:
    def preFind(self, A, B, l, h):
        ans = -1
        while l <= h:
            mid = (l + h) // 2
            if A[mid] == B:
                ans = mid
                h = mid - 1

            if A[mid] > B:
                h = mid - 1
            else:
                l = mid + 1

        return ans

    def postFind(self, A, B, l, h):
        ans = -1
        while l <= h:
            mid = (l + h) // 2
            if A[mid] == B:
                ans = mid
                l = mid + 1

            if A[mid] > B:
                h = mid - 1
            else:
                l = mid + 1

        return ans

    def searchRange(self, A, B):
        n = len(A)
        l = self.preFind(A, B, 0, n-1)
        if l == -1:
            return [-1, -1]
        h = self.postFind(A, B, l, n-1)
        return [l, h]

if __name__ == '__main__':
    A = [5, 7, 7, 8, 8, 8, 10]
    B = 8
    C = Solution()
    print(C.searchRange(A, B))

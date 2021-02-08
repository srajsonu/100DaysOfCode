import sys
sys.setrecursionlimit(10 ** 9)
class Solution:
    def merge_sort(self, A, l, h):
        if l < h:
            mid = (l + h) // 2
            left = self.merge_sort(A, l, mid)
            right = self.merge_sort(A, mid+1, h)
            return self.merge(left, right, A)

        # n = len(A)
        # if n <= 1:
        #     return A
        #
        # mid = n // 2
        # left = self.merge_sort(A[:mid])
        # right = self.merge_sort(A[mid:])
        # return self.merge(left, right, A)

    def merge(self, l, r, ans):
        i = 0
        j = 0
        k = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                ans[k] = l[i]
                i += 1
            else:
                ans[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            ans[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            ans[k] = r[j]
            j += 1
            k += 1

        return ans

    def solve(self, A):
        n = len(A)
        return self.merge_sort(A, 0, n-1)

if __name__ == '__main__':
    A = [5, 3, 2, 9, 8, 7]
    B = Solution()
    print(B.solve(A))

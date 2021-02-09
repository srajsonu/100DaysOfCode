class Solution:
    def merge_sort(self, A, tmp, l, r):
        mod = 10 ** 9 + 7
        inv = 0
        if l < r:
            mid = (l + r) // 2
            inv += self.merge_sort(A, tmp, l, mid)
            inv += self.merge_sort(A, tmp, mid+1, r)
            inv += self.merge(A, tmp, l, mid, r)
            inv %= mod

        return inv

    def merge(self, A, tmp, l, mid, r):
        mod = 10 ** 9 + 7
        i = l
        j = mid + 1
        k = l
        inv = 0
        while i <= mid and j <= r:
            if A[i] <= A[j]:
                tmp[k] = A[i]
                i += 1
            else:
                inv += (mid - i + 1)
                tmp[k] = A[j]
                j += 1

            k += 1

        while i <= mid:
            tmp[k] = A[i]
            k += 1
            i += 1

        while j <= r:
            tmp[k] = A[j]
            j += 1
            k += 1

        for i in range(l, r+1):
            A[i] = tmp[i]

        return inv

    def solve(self, A):
        n = len(A)
        tmp = [0 for _ in range(n)]
        return self.merge_sort(A, tmp, 0, n-1)

if __name__ == '__main__':
    A = [3, 2, 1, 4, 5]
    B = Solution()
    print(B.solve(A))

from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

class Solution:
    def Partition(self, A, l, h):
        pivot = A[h]
        cnt = 0
        for i in A:
            if i <= pivot:
                cnt += 1

        while l <= cnt and h > cnt:
            while A[l] <= pivot:
                l += 1
            while A[h] > pivot:
                h -= 1

            A[l], A[h] = A[h], A[l]

        return l+1

    def QuickSort(self, A, l, h):
        n = len(A)
        if l < h:
            mid = self.Partition(A, 0, n-1)
            self.QuickSort(A, 0, mid-1)
            self.QuickSort(A, mid+1, h)



if __name__ == '__main__':
    A = [4, 9, 3, 2, 5, 7]
    B = Solution()
    print(B.QuickSort(A, 0, len(A)-1))

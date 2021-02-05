from bisect import bisect_right


class Solution:
    def findMedian(self, A):
        m = len(A)
        n = len(A[0])
        mn = float('inf')
        mx = float('-inf')

        for i in A:
            mn = min(mn, i[0])
            mx = max(mx, i[-1])

        req = (1 + m*n) // 2

        while mn <= mx:
            mid = (mn + mx) // 2
            cnt = 0
            for i in A:
                cnt += bisect_right(i, mid)

            if cnt < req:
                mn = mid + 1
            else:
                mx = mid - 1

        return mn

if __name__ == '__main__':
    A = [[1, 3, 5],
         [2, 6, 9],
         [3, 6, 9]]
    B = Solution()
    print(B.findMedian(A))

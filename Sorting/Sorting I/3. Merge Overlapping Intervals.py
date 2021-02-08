class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def solve(self, A):
        ans = []
        n = len(A)
        A = sorted(A, key=lambda k: k.start)
        ans.append(A[0])
        for i in range(1, n):
            tmp = A[i]
            if tmp.start <= ans[-1].end and tmp.end > ans[-1].end:
                ans[-1].end = tmp.end

            if tmp.start > ans[-1].end:
                ans.append(tmp)

        return ans

if __name__ == '__main__':
    A = [[1, 3],
         [2, 6],
         [8, 10],
         [15, 18]]
    B = Solution()
    print(B.solve(A))

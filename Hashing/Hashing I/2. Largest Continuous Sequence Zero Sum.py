class Solution:
    def lszero(self, A):
        n = len(A)
        freq = {}
        pre = [0 for _ in range(n)]
        pre[0] = A[0]
        for i in range(1, n):
            pre[i] += pre[i-1] + A[i]


        curr_cnt = 0
        max_count = 0
        curr_ans = []
        ans = []
        for i in range(n):
            if pre[i] == 0:
                curr_cnt = i + 1
                curr_ans = A[:i + 1]
                if max_count < curr_cnt:
                    max_count = curr_cnt
                    ans = curr_ans

            if pre[i] not in freq:
                freq[pre[i]] = i
            else:
                curr_cnt = abs(i - freq[pre[i]])
                curr_ans = A[freq[pre[i]]+1: i+1]
                if max_count < curr_cnt:
                    max_count = curr_cnt
                    ans = curr_ans

        return ans

if __name__ == '__main__':
    A = [-8, 8, -1, -16, -28, -27, 15, -14, 14, -27, -5, -6, -25, -11, 28, 29, -3, -25, 17, -25, 4, -20, 2, 1, -17, -10, -25]
    B = Solution()
    print(B.lszero(A))

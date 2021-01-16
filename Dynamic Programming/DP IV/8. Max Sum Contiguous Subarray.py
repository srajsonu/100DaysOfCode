class Solution:
    def maxSubArray(self, A):
        n = len(A)
        max_ans = A[0]
        curr_max = A[0]

        for i in range(1, n):
            curr_max = max(curr_max + A[i], A[i])
            max_ans = max(max_ans, curr_max)

        return max_ans

if __name__ == '__main__':
    A = [1, 2, 3, 4, -10]
    B = Solution()
    print(B.maxSubArray(A))

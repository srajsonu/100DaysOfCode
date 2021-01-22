class Solution:
    def maxProfit(self, A):
        n = len(A)
        bought = float('inf')
        profit = 0
        for i in range(n):
            bought = min(bought, A[i])
            profit = max(profit, A[i] - bought)

        return profit

if __name__ == '__main__':
    A = [1, 4, 5, 2, 4]
    B = Solution()
    print(B.maxProfit(A))

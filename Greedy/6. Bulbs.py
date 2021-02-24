class Solution:
    def bulbs(self, A):
        n = len(A)
        state = 0
        ans = 0

        for i in range(n):
            if A[i] == state:
                ans += 1
                state = 1 - state

        return ans




if __name__ == '__main__':
    A = [0, 1, 0, 1]
    B = Solution()
    print(B.bulbs(A))

class Solution:
    def solve(self, A):
        n = len(A)
        ans = 0
        l = 0
        h = n-1

        while l < h:
            area = 0
            if A[l] <= A[h]:
                area = (h - l) * A[l]
                l += 1
            else:
                area = (h - l) * A[h]
                h -= 1

            ans = max(area, ans)

        return ans

if __name__ == '__main__':
    A = [1, 5, 4, 3]
    B = Solution()
    print(B.solve(A))

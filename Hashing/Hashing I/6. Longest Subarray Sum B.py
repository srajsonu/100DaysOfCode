class Solution:
    def solve(self, A, B):
        n = len(A)
        freq = {}
        sm = 0
        ans = -1
        for i in range(n):
            sm += A[i]
            if sm not in freq:
                freq[sm] = i

            if sm == B:
                ans = i + 1

            if sm - B in freq:
                index = freq[sm-B]
                if ans < (i - index):
                    ans = i - index

        return ans

if __name__ == '__main__':
    A = [-3, -3, -3, 3, -3, -4, 4, 5, 3, 4, -4 ]
    B = 4
    C = Solution()
    print(C.solve(A, B))

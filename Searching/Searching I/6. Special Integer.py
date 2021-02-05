class Solution:
    def solve(self, A, B):
        n = len(A)
        l = 1
        h = n
        ans = 0
        while l <= h:
            mid = (l + h) // 2
            sm = sum(A[:mid])
            if sm > B:
                h = mid - 1
                continue

            for i in range(mid, n):
                sm += A[i] - A[i-mid]
                if sm > B:
                    h = mid - 1
                    break
            else:
                l = mid + 1
                ans = mid

        return ans


if __name__ == '__main__':
    A = [5, 10, 20, 100, 105]
    B = 130
    C = Solution()
    print(C.solve(A, B))

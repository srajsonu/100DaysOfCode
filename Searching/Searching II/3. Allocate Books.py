class Solution:
    def solve(self, A, B):
        l = max(A)
        h = sum(A)

        while l <= h:
            mid = (l + h) // 2
            req = 1
            sm = 0
            for i in A:
                sm += i
                if sm > mid:
                    req += 1
                    sm = i
            if req <= B:
                h = mid - 1
            else:
                l = mid + 1

        return l


if __name__ == '__main__':
    A = [12, 34, 67, 90]
    B = 2
    C = Solution()
    print(C.solve(A, B))

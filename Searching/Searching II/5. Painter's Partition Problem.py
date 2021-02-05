class Solution:
    def paint(self, A, B, C):
        mod = 10000003
        n = len(C)
        if A >= n:
            return max(C) * B

        l = max(C)
        h = sum(C)
        while l <= h:
            mid = (l + h) // 2
            req = 1
            sm = 0

            for i in C:
                sm += i
                if sm > mid:
                    req += 1
                    sm = i

            if req <= A:
                h = mid - 1
            else:
                l = mid + 1

        return (l * B) % mod


if __name__ == '__main__':
    A = 3
    B = 10
    C = [185, 186, 938, 558, 655, 461, 441, 234, 902, 681]
    D = Solution()
    print(D.paint(A, B, C))

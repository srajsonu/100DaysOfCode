class Solution:
    def solve(self, A):
        A = [float(i) for i in A]
        n = len(A)
        if n < 3:
            return 0

        a = A[0]
        b = A[1]
        c = A[2]

        for i in range(3, n):
            if 1 < (a+b+c) and (a+b+c) < 2:
                return 1

            if (a + b + c) >= 2:
                if a > b and a > c:
                    a = A[i]
                elif b > a and b > c:
                    b = A[i]
                else:
                    c = A[i]
            else:
                if a < b and a < c:
                    a = A[i]
                elif b < c and b < a:
                    b = A[i]
                else:
                    c = A[i]

        if (a + b + c) > 1 and (a + b + c) < 2:
            return 1

        return 0


if __name__ == '__main__':
    A = [ "0.366507", "0.234601", "2.126313", "1.372403", "2.022170", "0.308558", "2.120754", "1.561462" ]
    B = Solution()
    print(B.solve(A))

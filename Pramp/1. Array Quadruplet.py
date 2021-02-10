class Solution:
    def solve(self, A, B):
        n = len(A)
        A.sort()
        if n < 4:
            return []
        for i in range(n-3):
            for j in range(i+1, n-2):
                req = B - (A[i] + A[j])
                l = j+1
                h = n-1
                while l < h:
                    if A[l] + A[h] < req:
                        l += 1
                    elif A[l] + A[h] > req:
                        h -= 1
                    else:
                        return [A[i], A[j], A[l], A[h]]

        return []

if __name__ == '__main__':
    A = [4, 4, 4, 4]
    B = 16
    C = Solution()
    print(C.solve(A, B))

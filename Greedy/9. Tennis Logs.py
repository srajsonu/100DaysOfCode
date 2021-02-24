class Solution:
    def solve(self, A, B):
        if B[0] == 3:
            'No'

        global w, l
        if B[0] == 1:
            w = 1
            l = 2
        else:
            w = 2
            l = 1

        i = 0
        while i < A:
            if B[i] == w or B[i] == l:
                if B[i] == w:
                    l ^= w
                else:
                    w ^= l
            else:
                return 'No'

            i += 1

        return 'Yes'


if __name__ == '__main__':
    A = 3
    B = [3, 1, 1]
    C = Solution()
    print(C.solve(A, B))

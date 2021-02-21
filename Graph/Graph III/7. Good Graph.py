class Solution:
    def find_root(self, A, parent):
        if parent[A] == A:
            return A
        return self.find_root(parent[A], parent)

    def union(self, A, B, parent, height):
        C = self.find_root(A, parent)
        D = self.find_root(B, parent)

        if C == D:
            return

        if height[C] < height[D]:
            parent[C] = D
        elif height[D] < height[C]:
            parent[D] = C
        else:
            parent[D] = C
            height[C] += 1

        self.ans -= 1


    def solve(self, A):
        n = len(A)
        parent = [i for i in range(n+1)]
        height = [0 for _ in range(n+1)]

        self.ans = n
        for i, j in enumerate(A):
            if j != 1:
                self.union(i+1, j, parent, height)
            else:
                self.ans -= 1

        return self.ans


if __name__ == '__main__':
    A =  [1, 2, 1, 2]
    B = Solution()
    print(B.solve(A))

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
        elif height[C] > height[D]:
            parent[D] = C
        else:
            parent[D] = C
            height[C] += 1

    def solve(self, A):
        n = len(A)
        parent = [i for i in range(20000)]
        height = [0 for _ in range(20000)]

        for i, j in A:
            self.union(i, j+10000, parent, height)

        ans = set()
        for i, j in A:
            ans.add(self.find_root(i, parent))

        return n - len(ans)


if __name__ == '__main__':
    A = [[0, 0],
         [0, 1],
         [1, 0],
         [1, 2],
         [2, 2],
         [2, 1]]
    B = Solution()
    print(B.solve(A))

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
            parent[C] = D
            height[C] += 1

    def solve(self, A, B):
        parent = [i for i in range(A)]
        height = [0 for _ in range(A)]
        B = sorted(B, key=lambda i: i[2])
        mst = 0

        for i, j, k in B:
            C = self.find_root(i-1, parent)
            D = self.find_root(j-1, parent)

            if C == D:
                continue

            self.union(C, D, parent, height)
            mst += k

        return mst


if __name__ == '__main__':
    A = 4
    B = [[1, 2, 1],
         [2, 3, 4],
         [1, 4, 3],
         [4, 3, 2],
         [1, 3, 10]]
    C = Solution()
    print(C.solve(A, B))

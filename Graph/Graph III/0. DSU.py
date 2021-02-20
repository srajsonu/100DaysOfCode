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


    def solve(self, A, B, C):
        parent = [i for i in range(A)]
        height = [0 for _ in range(A)]

        for i, j in zip(B, C):
            D = self.find_root(i-1, parent)
            E = self.find_root(j-1, parent)

            if D == E:
                continue

            self.union(D, E, parent, height)

        return parent, height

if __name__ == '__main__':
    A = 5
    B = [1, 3, 3, 5]
    C = [3, 2, 4, 1]
    D = Solution()
    print(D.solve(A, B, C))

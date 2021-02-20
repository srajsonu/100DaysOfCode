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

    def solve(self, A, B):
        parent = [i for i in range(A)]
        height = [0 for _ in range(A)]

        ans = []
        for i, j, k in B:
            if i == 0:
                self.union(j-1, k-1, parent, height)
            else:
                C = self.find_root(j-1, parent)
                D = self.find_root(k-1, parent)

                if C == D:
                    ans.append(1)
                else:
                    ans.append(0)

        return ans


if __name__ == '__main__':
    A = 4
    B = [[0, 1, 2],
         [0, 2, 3],
         [1, 1, 3],
         [0, 3, 4],
         [0, 4, 3],
         [1, 1, 4]]
    C = Solution()
    print(C.solve(A, B))

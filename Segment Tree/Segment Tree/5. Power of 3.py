from math import ceil, log2


class Solution:
    def build(self, arr, tree, s, e, node):
        if s == e:
            tree[node] = int(arr[s])
            return

        mid = (s + e) // 2

        self.build(arr, tree, s, mid, 2 * node + 1)
        self.build(arr, tree, mid + 1, e, 2 * node + 2)
        print(s, e, mid)
        tree[node] = (2 ** abs(e-mid)) * tree[2 * node + 1] + tree[2 * node + 2]

    def update(self, arr, tree, s, e, node, idx):
        if s == e:
            if arr[idx] == 0:
                arr[idx] = 1
                tree[node] = arr[idx]
            return

        mid = (s + e) // 2
        if idx > mid:
            self.update(arr, tree, mid + 1, e, 2 * node + 2, idx)
        else:
            self.update(arr, tree, s, mid, 2 * node + 1, idx)

        tree[node] = (2 ** abs(e-mid)) * tree[2 * node + 1] + tree[2 * node + 2]

    def query(self, arr, tree, s, e, node, l, h):
        if s > h or e < l:
            return 0

        if s >= l and e <= h:
            return tree[node]

        mid = (s + e) // 2
        ans1 = self.query(arr, tree, s, mid, 2 * node + 1, l, h)
        ans2 = self.query(arr, tree, mid + 1, e, 2 * node + 2, l, h)
        return ans1 + ans2

    def solve(self, A, B):
        arr = [int(i) for i in A]
        n = len(arr)
        tree = [0 for _ in range(4 * n)]
        ans = []

        self.build(arr, tree, 0, n - 1, 0)
        print(tree)
        for i, j, k in B:
            if i == 0:
                tmp = self.query(arr, tree, 0, n - 1, 0, j - 1, k - 1)
                ans.append(tmp % 3)
            else:
                self.update(arr, tree, 0, n - 1, 0, j - 1)
                ans.append(k)

        return ans


if __name__ == '__main__':
    A = '10010'
    B = [[0, 3, 5],
         [0, 3, 4],
         [1, 2, -1],
         [0, 1, 5]]
    C = Solution()
    print(C.solve(A, B))

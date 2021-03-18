class Solution:
    def build(self, arr, tree, s, e, node):
        if s == e:
            tree[node] = arr[s]
            return

        mid = (s + e) // 2
        self.build(arr, tree, s, mid, 2 * node + 1)
        self.build(arr, tree, mid + 1, e, 2 * node + 2)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    def update(self, arr, tree, s, e, node, idx, val):
        if s == e:
            A[idx] = val
            tree[node] = arr[idx]
            return

        mid = (s + e) // 2

        if idx > mid:
            self.update(arr, tree, mid + 1, e, 2 * node + 2, idx, val)
        else:
            self.update(arr, tree, s, mid, 2 * node + 1, idx, val)

        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    def query(self, arr, tree, s, e, node, l, h):
        if s > h or e < l:
            return 0

        if s >= l and e <= h:
            return tree[node]

        mid = (s + e) // 2
        ans1 = self.query(arr, tree, s, mid, 2 * node + 1, l, h)
        ans2 = self.query(arr, tree, mid + 1, e, 2 * node + 2, l, h)
        return ans1 + ans2

    def solve(self, A):
        n = len(A)
        tree = [0 for _ in range(4 * n)]
        self.build(A, tree, 0, n - 1, 0)
        return tree


if __name__ == '__main__':
    A = [2, 3, 1, 7, 6, -1, 3]
    B = Solution()
    print(B.solve(A))

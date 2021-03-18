class Solution:
    def update(self, arr, tree, s, e, node, idx):
        if s == e:
            arr[idx] += 1
            tree[node] = arr[idx]
            return

        mid = (s + e) // 2
        if idx > mid:
            self.update(arr, tree, mid+1, e, 2 * node + 2, idx)
        else:
            self.update(arr, tree, s, mid, 2 * node + 1, idx)

        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    def update1(self, arr, tree, s, e, node, idx):
        if s == e:
            if arr[idx] > 0:
                arr[idx] -= 1
                tree[node] = arr[idx]
            return

        mid = (s + e) // 2
        if idx > mid:
            self.update1(arr, tree, mid+1, e, 2 * node + 2, idx)
        else:
            self.update1(arr, tree, s, mid, 2 * node + 1, idx)

        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

    def query(self, arr, tree, s, e, node, l, h):
        if s > h or e < l:
            return 0

        if s >= l and e <= h:
            return tree[node]

        mid = (s + e) // 2
        ans1 = self.query(arr, tree, s, mid, 2 * node + 1, l, h)
        ans2 = self.query(arr, tree, mid+1, e, 2 * node + 2, l, h)
        return ans1 + ans2


    def solve(self, A, B):
        arr = [0 for _ in range(A)]
        tree = [0 for _ in range(4 * A)]
        ans = []
        for i, j, k in B:
            if i == 1:
                self.update(arr, tree, 0, A-1, 0, j)
            elif i == 2:
                self.update1(arr, tree, 0, A-1, 0, j)
            else:
                tmp = self.query(arr, tree, 0, A-1, 0, j, k)
                ans.append(tmp)

        return ans


if __name__ == '__main__':
    A = 5
    B = [[1, 1, -1],
         [1, 2, -1],
         [1, 3, -1],
         [3, 1, 3],
         [3, 2, 4]]
    C = Solution()
    print(C.solve(A, B))

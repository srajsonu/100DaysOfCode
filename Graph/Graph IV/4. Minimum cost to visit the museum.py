from collections import defaultdict, deque


class Solution:
    def solve(self, A, B, C, D):
        n = len(A)
        graph = defaultdict(list)

        for i, j, k in zip(B, C, D):
            graph[i-1].append((j-1, k))
            graph[j-1].append((i-1, k))

        ans = A
        for i in range(n):
            q = deque()
            q.append((i, A[i]))
            while q:
                curr, w = q.popleft()
                for nxt_node, wt in graph[curr]:
                    new_wt = w + wt
                    if new_wt < ans[nxt_node]:
                        ans[nxt_node] = new_wt
                        q.append((nxt_node, new_wt))

        return ans


if __name__ == '__main__':
    A = [1, 2, 3, 1, 5]
    B = [1, 2, 3, 4]
    C = [2, 3, 4, 5]
    D = [1, 1, 1, 1]
    E = Solution()
    print(E.solve(A, B, C, D))

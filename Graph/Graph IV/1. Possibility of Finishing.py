from collections import defaultdict, deque


class Solution:
    def solve(self, A, B, C):
        graph = defaultdict(list)

        for i, j in zip(B, C):
            graph[i-1].append(j-1)

        inDegree = [0 for _ in range(A)]

        for i in graph:
            for j in graph[i]:
                inDegree[j] += 1

        q = deque()
        for i in range(A):
            if inDegree[i] == 0:
                q.append(i)

        ans = 0
        while q:
            curr = q.popleft()
            ans += 1

            for nxt_node in graph[curr]:
                inDegree[nxt_node] -= 1
                if inDegree[nxt_node] == 0:
                    q.append(nxt_node)

        return 1 if ans == A else 0


if __name__ == '__main__':
    A = 3
    B = [1, 2]
    C = [2, 3]
    D = Solution()
    print(D.solve(A, B, C))

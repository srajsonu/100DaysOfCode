from collections import defaultdict, deque


class Solution:
    def dfs(self, v, vis): #DFS implementation on Topological Sort
        vis.add(v)
        for w in self.graph[v]:
            if w not in vis:
                vis.add(w)
                self.dfs(w, vis)

        self.stack.append(v)

    def sort(self, A, B):
        self.graph = defaultdict(list)
        self.stack = []

        for i, j in B:
            self.graph[i].append(j)

        vis = set()
        for i in range(A):
            if i not in vis:
                self.dfs(i, vis)

        ans = []
        while self.stack:
            ans.append(self.stack.pop())

        return ans


    def solve(self, A, B):
        graph = defaultdict(list)

        for i, j in B:
            graph[i].append(j)

        inDegree = [0 for _ in range(A)]

        for i in graph:
            for j in graph[i]:
                inDegree[j] += 1

        q = deque()
        for i in range(A):
            if inDegree[i] == 0:
                q.append(i)

        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for nxt_node in graph[curr]:
                inDegree[nxt_node] -= 1
                if inDegree[nxt_node] == 0:
                    q.append(nxt_node)

        return ans



if __name__ == '__main__':
    A = 4
    B = [[0, 1],
         [0, 2],
         [1, 3],
         [2, 3],
         [2, 1]]

    C = Solution()
    print(C.solve(A, B))
    print(C.sort(A, B))

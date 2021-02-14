from collections import deque


class Solution:
    def slidingMaximum(self, A, B):
        n = len(A)
        q = deque()
        ans = []
        for i in range(n):
            while q and A[q[-1]] <= A[i]:
                q.pop()

            q.append(i)
            if i >= B-1:
                ans.append(A[q[0]])

            if q[0] == i-B+1:
                q.popleft()

        return ans

if __name__ == '__main__':
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    B = 3
    C = Solution()
    print(C.slidingMaximum(A, B))

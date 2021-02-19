from collections import deque


class Solution:
    def multiple(self, A):
        q = deque()
        vis = set([])
        s = '1'
        q.append(s)

        while q:
            s = q.popleft()

            rem = int(s) % A

            if rem == 0:
                return s

            if rem not in vis:
                vis.add(rem)
                q.append(s + '0')
                q.append(s + '1')


if __name__ == '__main__':
    A = 55
    B = Solution()
    print(B.multiple(A))

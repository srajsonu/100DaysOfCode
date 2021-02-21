class Solution:
    def solve(self, A, N):
        vis = set()

        for i in A:
            if i not in vis:
                if i == 'start' or i == 'restart':
                    vis.add(i)
                elif i == 'stop' and ('start' in vis or 'restart' in vis):
                    if 'start' in vis:
                        vis.remove('start')
                    elif 'restart' in vis:
                        vis.remove('restart')
                elif i == 'stop' and ('start' not in vis or 'restart' not in vis):
                    vis.add(i)

        return '200' if not vis or ('restart' or 'start') in vis else '404'


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(str, input().split()))
        print(S.solve(A, N))

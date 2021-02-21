class Solution:
    def solve(self, A):
        freq = {}

        for i in A:
            freq[i] = True

        for i in ['P', 'C', 'M']:
            if i in freq:
                return 'YES'

        return 'NO'


if __name__ == '__main__':
    S = Solution()
    T = int(input())
    for _ in range(T):
        A = input()
        print(S.solve(A))

class Solution:
    def CountSort(self, A, col):
        n = len(A)
        mn = ord(' ')
        mx = ord('z')
        ans = [0 for _ in range(n)]
        freq = [0 for _ in range(mn, mx+1)]

        for item in A:
            char = ord(item[col]) - mn if col < len(item) else 0 # 2 -> ord('2') - mn = 50 - 48 = 2
            freq[char] += 1

        for i in range(1, len(freq)):
            freq[i] += freq[i-1]

        for item in A:
            char = ord(item[col]) - mn if col < len(item) else 0
            ans[freq[char]-1] = item
            freq[char] -= 1

        return A


    def solve(self, A):
        n = len(A)
        max_col = len(max(A, key=len))
        # for i in range(n):
        #     A[i] = A[i].replace(' ', '0')
        #     A[i] = (max_col - len(A[i])) * '0' + A[i]

        for col in range(max_col-1, -1, -1):
            A = self.CountSort(A, col)

        return A

if __name__ == '__main__':
    A = ['zld 93 12',
         'fp kindle book',
         '10a echo show',
         '17g 12 25 b',
         'ab1 kindle book',
         '125 echo dot second generation']
    B = Solution()
    print(B.solve(A))

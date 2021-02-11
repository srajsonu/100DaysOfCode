class Solution:
    def longestConsecutive(self, A):
        freq = {}
        for i in A:
            freq[i] = True

        ans = 0
        for i in A:
            if i-1 not in freq:
                k = i
                cnt = 0
                while k in freq:
                    k += 1
                    cnt += 1
                ans = max(cnt, ans)

        return ans

if __name__ == '__main__':
    A = [100, 4, 200, 1, 3, 2]
    B = Solution()
    print(B.longestConsecutive(A))

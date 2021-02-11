class Solution:
    def lengthOfLongestSubstring(self, A):
        n = len(A)
        freq = {}
        cnt = 0
        ans = 0
        for i in range(n):
            if A[i] not in freq:
                cnt += 1
                freq[A[i]] = i
            else:
                prev = freq[A[i]]
                cnt = min(i - prev, cnt + 1)
                freq[A[i]] = i

            ans = max(ans, cnt)

        return ans


if __name__ == '__main__':
    A = "dadbc"
    B = Solution()
    print(B.lengthOfLongestSubstring(A))

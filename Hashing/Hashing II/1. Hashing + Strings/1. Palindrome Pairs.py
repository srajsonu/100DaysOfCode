class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

    def solve(self, A):
        n = len(A)
        freq = {}
        for i in range(n):
            freq[A[i]] = i

        ans = []
        for i in range(n):
            for j in range(len(A[i])+1):
                pre = A[i][:j]
                suf = A[i][j:]
                if self.isPalindrome(pre):
                    if suf[::-1] in freq and freq[suf[::-1]] != i:
                        ans.append([freq[suf[::-1]], i])

                if suf and self.isPalindrome(suf):
                    if pre[::-1] in freq and freq[pre[::-1]] != i:
                        ans.append([i, freq[pre[::-1]]])
        return ans

if __name__ == '__main__':
    A = ["abcd", "dcba", "lls", "s", "sssll"]
    B = Solution()
    print(B.solve(A))

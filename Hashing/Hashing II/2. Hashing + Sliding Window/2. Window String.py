class Solution:
    def minWindow(self, A, B):
        m = len(A)
        n = len(B)

        if m < n:
            return ''

        freqA = {}
        freqB = {}

        for i in B:
            if i not in freqB:
                freqB[i] = 1
            else:
                freqB[i] += 1
        cnt = 0
        i, j = 0, 0
        while j < m:
            if A[j] not in freqA:
                freqA[A[j]] = 1
            else:
                freqA[A[j]] += 1

            j += 1

        return freqA, freqB

if __name__ == '__main__':
    A = "ADOBECODEBANC"
    B = "ABC"
    C = Solution()
    print(C.minWindow(A, B))

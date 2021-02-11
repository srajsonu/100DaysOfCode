class Solution:
    def solve(self, A, B):
        m = len(A)
        n = len(B)
        freqA = {}
        freqB = {}

        for i in A:
            if i not in freqA:
                freqA[i] = 1
            else:
                freqA[i] += 1
        for j in B:
            if j not in freqB:
                freqB[j] = 1
            else:
                freqB[j] += 1
        cnt = 0
        for i in range(m):
            cnt += (freqA[A[i]]-1) * (freqB[B[i]] - 1)

        return cnt

if __name__ == '__main__':
    A = [1, 1, 2, 3, 3]
    B = [1, 2, 1, 2, 1]
    C = Solution()
    print(C.solve(A, B))

class Solution:
    def solve(self, A, B):
        freq = {}
        ans = []
        for i, j in enumerate(A):
            B[i] = '0' * (20 - len(B[i])) + B[i]
            B[i] = ''.join([str(int(k)%2) for k in B[i]])
            if j == '+':
                if B[i] not in freq:
                    freq[B[i]] = 1
                else:
                    freq[B[i]] += 1
            elif j == '-':
                if B[i] in freq:
                    freq[B[i]] -= 1
            else:
                if B[i] in freq:
                    ans.append(freq[B[i]])
                else:
                    ans.append(0)

        return ans

if __name__ == '__main__':
    A = ['+', '+', '?', '+', '-', '?']
    B = ['1', '241', '1', '361', '241', '101']
    C = Solution()
    print(C.solve(A, B))

class Solution:
    def solve(self, A):
        n = len(A)
        vis = set()
        stack = []
        freq = {}

        for i in A:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for i in range(n):
            freq[A[i]] -= 1
            if A[i] in vis:
                continue

            while stack and stack[-1] > A[i] and freq[stack[-1]] > 0:
                tmp = stack.pop()
                vis.remove(tmp)

            stack.append(A[i])
            vis.add(A[i])

        return "".join(stack)

if __name__ == '__main__':
    A = "cbacdcbc"
    B = Solution()
    print(B.solve(A))

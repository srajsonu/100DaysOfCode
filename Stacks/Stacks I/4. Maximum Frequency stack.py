from collections import defaultdict


class Solution:
    def push(self, j):
        if j not in self.freq:
            self.freq[j] = 1
        else:
            self.freq[j] += 1

        self.stack_freq[self.freq[j]] += [j]
        self.highest_freq = max(self.highest_freq, self.freq[j])
        self.stack.append(j)
        return -1

    def pop(self):
        ans = self.stack_freq[self.highest_freq].pop()
        self.freq[ans] -= 1
        if not self.stack_freq[self.highest_freq]:
            self.highest_freq -= 1
        return ans

    def solve(self, A):
        self.highest_freq = 0
        self.stack = []
        ans = []
        self.freq = {}
        self.stack_freq = defaultdict(list)
        for i, (j, k) in enumerate(A):
            if j == 1:
                val = self.push(k)
                ans.append(val)
            else:
                val = self.pop()
                ans.append(val)

        return ans


if __name__ == '__main__':
    A = [[1, 5],
         [1, 7],
         [1, 5],
         [1, 7],
         [1, 4],
         [1, 5],
         [2, 0],
         [2, 0],
         [2, 0],
         [2, 0]]

    B = Solution()
    print(B.solve(A))

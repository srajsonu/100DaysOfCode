class Solution:
    def anagrams(self, A):
        n = len(A)
        freq = {}
        for i in range(n):
            tmp = "".join(sorted(A[i]))
            if tmp not in freq:
                freq[tmp] = [i + 1]
            else:
                freq[tmp] += [i + 1]

        return list(freq.values())

if __name__ == '__main__':
    A = ['cat', 'dog', 'god', 'tca']
    B = Solution()
    print(B.anagrams(A))

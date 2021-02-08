
class Solution:
    def make_comparator(self, less_than):
        def compare(x, y):
            if less_than(x, y):
                return -1
            elif less_than(y, x):
                return 1
            else:
                return 0

        return compare

    def sort(self, s1, s2):
        s1 = str(s1)
        s2 = str(s2)

        if int(s1 + s2) > int(s2 + s1):
            return True
        return False

    def solve(self, A):
        n = len(A)
        ans = []

        return


if __name__ == '__main__':
    A = [3, 30, 34, 5, 9]
    B = Solution()
    print(B.solve(A))

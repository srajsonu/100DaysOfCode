from heapq import *


class Solution:
    def solve(self, A, B):
        heapify(A)

        while B:
            tmp = heappop(A)
            if tmp == 0:
                heappush(A, tmp)
                break
            elif tmp > 0:
                if B % 2 == 0:
                    heappush(A, tmp)
                    break
                else:
                    heappush(A, -tmp)
                    break
            else:
                heappush(A, -tmp)

            B -= 1


        return sum(A)

if __name__ == '__main__':
    A = [24, -68, -29, -9, 84]
    B = 4
    C = Solution()
    print(C.solve(A, B))

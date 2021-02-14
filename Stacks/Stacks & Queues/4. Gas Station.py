class Solution:
    def canCompleteCircuit(self, A, B):
        n = len(A)
        total_gas = 0
        total_cost = 0
        start = 0
        tank = 0
        for i in range(n):
            total_gas += A[i]
            total_cost += B[i]
            tank += A[i] - B[i]

            if tank < 0:
                start = i + 1
                tank = 0

        if total_gas < total_cost:
            return -1
        else:
            return start


if __name__ == '__main__':
    A =  [1, 2]
    B =  [2, 1]
    C = Solution()
    print(C.canCompleteCircuit(A, B))

class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.min = -1
        self.cnt = 0

    def push(self, x):
        if not self.stack:
            self.min = x
            self.stack.append(x)

        elif x <= self.min:
            val = (2 * x) - self.min
            self.stack.append(val)
            self.min = x

        else:
            self.stack.append(x)

        self.cnt += 1

    # @return nothing
    def pop(self):
        if self.stack:
            tmp = self.stack.pop()
            if tmp <= self.min:
                val = (2 * self.min) - tmp
                self.min = val

            if not self.stack:
                self.min = -1

            self.cnt -= 1

    # @return an integer
    def top(self):
        return self.stack[self.cnt - 1] if self.stack else -1

    # @return an integer
    def getMin(self):
        return self.min

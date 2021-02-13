class Solution:
    def simplifyPath(self, A):
        stack = []
        n = len(A)
        i = 0
        while i < n:
            while i < n and A[i] == '/':
                i += 1
            start = i
            while i < n and A[i] != '/':
                i += 1
            ans = A[start:i]
            if ans == '..':
                if stack:
                    stack.pop()
            elif ans and ans != '.':
                stack.append(ans)

        if not stack:
            return '/'

        return '/' + '/'.join(stack)

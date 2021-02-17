from collections import defaultdict, deque


class ListNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def build(self, child, parent):
        if parent and child:
            self.graph[parent].append(child.val)
            self.graph[child.val].append(parent)

        if child.left:
            self.build(child.left, child.val)

        if child.right:
            self.build(child.right, child.val)

    def solve(self, root, B, C):
        self.build(root, None)
        q = deque()
        q.append((B, 1))
        vis = set()
        vis.add(B)
        ans = []
        while q:
            node, cnt = q.popleft()
            for nxt_node in self.graph[node]:
                if nxt_node not in vis:
                    if cnt == C:
                        ans.append(nxt_node)

                    q.append((nxt_node, cnt+1))
                    vis.add(nxt_node)

        return ans if C > len(q) else [B]

if __name__ == '__main__':
    root = ListNode(1)
    root.left = ListNode(2)
    root.right = ListNode(3)
    root.left.left = ListNode(4)
    root.left.right = ListNode(5)
    root.right.left = ListNode(6)
    root.right.right = ListNode(7)
    root.left.left.left = ListNode(8)

    B = 3
    C = 3
    D = Solution()
    print(D.solve(root, B, C))

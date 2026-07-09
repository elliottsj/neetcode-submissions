from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out = []
        Q = deque()
        Q.append(root)
        while len(Q) > 0:
            level_size = len(Q)
            current_level = []
            for _ in range(level_size):
                node = Q.popleft()
                current_level.append(node.val)
                if node.left is not None:
                    Q.append(node.left)
                if node.right is not None:
                    Q.append(node.right)
            out.append(current_level)
        return out
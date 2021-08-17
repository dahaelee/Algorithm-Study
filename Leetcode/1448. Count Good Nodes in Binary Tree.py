class Solution:
    def __init__(self):
        self.goods = 0

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_node):
            if root.val >= max_node:
                self.goods += 1

            max_node = max(max_node, root.val)

            if root.left:
                dfs(root.left, max_node)
            if root.right:
                dfs(root.right, max_node)

        dfs(root, root.val)
        return self.goods

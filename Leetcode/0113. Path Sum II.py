# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []

        if not root:
            return paths

        def dfs(node, path, tmp):
            if not node.left and not node.right:  # 리프노드면 경로 합 확인하고 리턴
                if tmp == targetSum:
                    paths.append(path)
                return

            if node.left:
                dfs(node.left, path + [node.left.val], tmp + node.left.val)
            if node.right:
                dfs(node.right, path + [node.right.val], tmp + node.right.val)

        dfs(root, [root.val], root.val)
        return paths

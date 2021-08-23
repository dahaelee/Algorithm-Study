class Solution:
    max_product = 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def set_node(node):
            if node.left:
                node.val += set_node(node.left)
            if node.right:
                node.val += set_node(node.right)

            return node.val

        def find_max_product(node, total):
            if not node:
                return

            product = node.val * (total - node.val)
            self.max_product = max(self.max_product, product)

            if node.left:
                find_max_product(node.left, total)
            if node.right:
                find_max_product(node.right, total)

        # 모든 노드의 값을 해당 노드가 루트인 트리의 합으로 설정
        set_node(root)

        # 트리 돌면서 노드 * (전체합-노드) 가 더 크면 최대값 갱신
        find_max_product(root, root.val)

        return self.max_product % (10 ** 9 + 7)

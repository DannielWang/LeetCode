class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def isLeafNode(node:TreeNode):
            if not node.left and not node.right:
                return
        def dfs(node:TreeNode):
            ans = 0
            if node.left:
                if isLeafNode(node.left):
                    ans += node.left.val
                else:
                    ans += dfs(node.left)
            if node.right and not isLeafNode(node.right):
                ans += dfs(node.right)
            return ans
        if root:
            return dfs(root)
        else:
            return 0
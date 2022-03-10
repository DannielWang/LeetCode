class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node: 'Node'):
            if not node:
                return
            ans.append(node.val)
            for ch in node.childen:
                dfs(ch)

        ans = []
        dfs(root)
        return ans

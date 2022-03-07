class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        res = []
        ans = []
        if m * n != r * c:
            return mat
        for i in range(n):
            for j in range(m):
                res.append(mat[i][j])
        for i in range(r):
            ans.append(res[:c])
            res = res[c:-1] + res[-1:]
        return ans
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        sum = [[0] * (n + 10) for _ in range(m + 10)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + img[i - 1][j - 1]
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                a, b = max(0, i - 1), max(0, j - 1)
                c, d = min(m - 1, i + 1), min(n - 1, j + 1)
                cnt = (c - a + 1) * (d - b + 1)
                tot = sum[c + 1][d + 1] - sum[a][d + 1] - sum[c + 1][b] + sum[a][b]
                ans[i][j] = tot // cnt
        return ans

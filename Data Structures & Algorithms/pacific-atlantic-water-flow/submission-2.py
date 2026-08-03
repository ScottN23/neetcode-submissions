class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or
                r not in range(rows) or
                c not in range(cols) or
                heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            prevHeight = heights[r][c]
            dfs(r + 1, c, visited, prevHeight)
            dfs(r - 1, c, visited, prevHeight)
            dfs(r, c + 1, visited, prevHeight)
            dfs(r, c - 1, visited, prevHeight)


        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if ((r, c) in pac and (r, c) in atl):
                    res.append([r, c])
        return res
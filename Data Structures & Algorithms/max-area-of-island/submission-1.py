class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        area = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            area = 1
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row = row + dr
                    col = col + dc
                    if (0 <= row < rows and
                        0 <= col < cols and
                        grid[row][col] == 1 and
                        (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))
                        area += 1
            return area
        
        def bfs(r, c):
            q = collections.deque([(r, c)])
            visited.add((r, c))
            area = 1  # Start with the initial cell counted

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (0 <= new_row < rows and 0 <= new_col < cols and 
                        grid[new_row][new_col] == 1 and 
                        (new_row, new_col) not in visited):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))
                        area += 1  # Increment the area for each cell added

            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))

        return area
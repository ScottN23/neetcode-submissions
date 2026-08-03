class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
            
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                currRow = dr + r
                currCol = dc + c
                if (currRow not in range(ROWS) or
                    currCol not in range(COLS) or
                    grid[currRow][currCol] == 1 or
                    (currRow, currCol) in visited):
                    continue
                queue.append((currRow, currCol))
                visited.add((currRow, currCol))
            length += 1
        return -1
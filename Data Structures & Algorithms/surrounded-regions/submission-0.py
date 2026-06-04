class Solution:

    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] !='O':
            return 
        
        sides = [
            (r+1, c),
            (r-1, c),
            (r, c+1),
            (r, c-1)
        ]
        grid[r][c] = 'T'

        for row, col in sides:
            self.dfs(grid, row, col)

    def solve(self, grid: List[List[str]]) -> None:
        row_len, col_len = len(grid), len(grid[0])

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 'O' and (i in [0, row_len -1] or j in [0, col_len - 1]):
                    self.dfs(grid, i, j)
        
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 'O':
                    grid[i][j] = 'X'
        
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 'T':
                    grid[i][j] = 'O'
        
        
        
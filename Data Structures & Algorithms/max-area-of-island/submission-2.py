class Solution:

    def dfs(self, grid, r,c ):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == 0:
            return 0
    
        grid[r][c] = 0
        current_area = 1
        sides = [
            (r-1, c),
            (r+1, c),
            (r, c-1),
            (r, c+1)
        ]

        for row, col in sides:
            current_area += self.dfs(grid, row, col)

        return current_area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row_len, col_len = len(grid), len(grid[0])
        max_area = 0
        current_area = 0

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    current_area = self.dfs(grid, i, j)
                    max_area = max(max_area, current_area)
        return max_area


    
    # def dfs(self, grid, r, c):
        
    #     if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == 0:
    #         return 0
    #     current_area = 1
    #     grid[r][c] = 0
    #     sides = [
    #         (r-1, c), # top
    #         (r, c-1), # left
    #         (r+1, c), # bottom
    #         (r, c+1) # right
    #     ]
    #     for row, col in sides:
    #         current_area += self.dfs(grid, row, col)
    #     return current_area 


    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     max_area = 0
        
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             if grid[i][j] == 1:
    #                 current_area = self.dfs(grid, i, j)
    #                 max_area = max(max_area, current_area)
    #     return max_area
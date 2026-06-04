class Solution:

    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == '0':
            return 
        
        grid[r][c] = '0'

        sides = [
            (r-1, c),
            (r+1, c),
            (r, c-1),
            (r, c+1)
        ]

        for row, col in sides:
            self.dfs(grid, row, col)
                

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row_len = len(grid)
        col_len = len(grid[0])
        count = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count 




    # def dfs(self, grid, r, c):

    #     if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == "0":
    #         return 
    #     grid[r][c] = "0"
    #     sides = [
    #         (r+1, c),
    #         (r-1, c),
    #         (r, c-1),
    #         (r, c+1)
    #     ]

    #     for row, col in sides:
    #         self.dfs(grid, row, col)



    # def numIslands(self, grid: List[List[str]]) -> int:
    #     if not grid:
    #         return
    #     count = 0

    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #             if grid[i][j] == "1":
    #                 self.dfs(grid, i, j)
    #                 count+=1

    #     return count
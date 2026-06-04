class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        row_len, col_len = len(grid), len(grid[0])

        from collections import deque 
        q = deque()
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        # list of treasure chest is in a queue 

        while q:
            r, c = q.popleft()

            sides = [
                (r+1, c),
                (r-1, c),
                (r, c-1),
                (r, c +1)
            ]

            for row, col in sides:
                if row < 0 or col < 0 or row >= row_len or col >= col_len or grid[row][col] != 2147483647:
                    continue
                grid[row][col] = grid[r][c] + 1
                q.append((row,col))
        
  




    ## THIS IS DFS SOLUTION
    # def dfs(self, grid, r, c, distance):
    #     if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] == -1:
    #         return 
        
    #     if grid[r][c] < distance:
    #         return 
    #     # update the current distance in the cell

    #     grid[r][c] = distance
    #     sides = [
    #         (r-1, c),
    #         (r+1, c),
    #         (r, c-1),
    #         (r, c+1)
    #     ]
    #     for row, col in sides:
    #         self.dfs(grid, row, col, distance + 1)

    # def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    #     row_len = len(grid)
    #     col_len = len(grid[0])

    #     for i in range(row_len):
    #         for j in range(col_len):
    #             if grid[i][j] == 0:
    #                 self.dfs(grid, i, j , 0)

    # THIS IS BFS SOLUTION
    # def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    #     from collections import deque
    #     row_len, col_len = len(grid), len(grid[0])
    #     q = deque()

    #     for i in range(row_len):
    #         for j in range(col_len):
    #             if grid[i][j] == 0:
    #                 q.append((i, j))

        

    #     while q:
    #         r, c = q.popleft()
    #         sides = [
    #             (r+1, c),
    #             (r-1, c),
    #             (r, c+1),
    #             (r, c-1)
    #         ]
    #         for row, col in sides:
    #             if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] != 2147483647:
    #                 continue
    #             grid[row][col] = grid[r][c] + 1
    #             q.append((row, col))




class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque 

        q = deque()
        fresh = 0

        row_len, col_len = len(grid), len(grid[0])
        
        # fresh fruits count
        # rotten are in quese

        for x in range(row_len):
            for y in range(col_len):
                if grid[x][y] == 1:
                    fresh += 1
                if grid[x][y] == 2:
                    q.append((x,y))

        minutes = 0

        # while is for processing until no more nodes exits
        while q and fresh > 0:
            # FOR loop: we are processing exactly one BFS level here
            for _ in range(len(q)):
                r, c = q.popleft()
                sides = [
                    (r -1, c),
                    (r +1, c),
                    (r, c -1),
                    (r, c +1)
                ]

                for row, col in sides:
                    if row < 0 or col < 0 or row >= row_len or col >= col_len or grid[row][col] != 1:
                        continue
                    
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row, col))

            minutes += 1

        return minutes if fresh == 0 else - 1

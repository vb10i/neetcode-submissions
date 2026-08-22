class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        dq = deque()
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    dq.append([r,c])

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        while dq and fresh>0:
            for i in range(len(dq)):
                r, c = dq.popleft()
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    if (row<0 or row == len(grid) or col<0 or col == len(grid[0]) or grid[row][col]!=1):
                        continue
                    grid[row][col] = 2
                    dq.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh==0 else -1
        

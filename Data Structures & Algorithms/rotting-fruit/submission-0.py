class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROW,COL = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        fresh = 0
        time = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh>0:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()
                
                for dr,dc in directions:
                    row,col = r+dr,c+dc
                    if(row in range(ROW) and col in range(COL) and grid[row][col]==1):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -=1
            time+=1
        
        if fresh == 0:
            return time
        else:
            return -1


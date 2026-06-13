class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROW,COL = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def addCell(r,c):
            if(min(r,c)<0 or r==ROW or c==COL or grid[r][c]==-1 or (r,c) in visit):
                return
            visit.add((r,c))
            q.append([r,c])
            
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            distance+=1
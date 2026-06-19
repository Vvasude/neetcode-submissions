class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #define the rows and cols
        ROWS,COLS = len(heights), len(heights[0])
        #cardinal directions
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        #sets for both the pacific and atlantic
        pac = [[False]* COLS for _ in range(ROWS)]
        atl = [[False]* COLS for _ in range(ROWS)]

        def bfs(source,ocean):
            q = deque(source)
            while q:
                r,c = q.popleft()
                #immediately flip to true
                ocean[r][c] = True
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if(0<=nr<ROWS and 0<=nc<COLS and not ocean[nr][nc] and heights[nr][nc]>=heights[r][c]):
                        q.append((nr,nc))
        
        
        #checks we throw at our BFS
        pacific = []
        atlantic = []
        for c in range(COLS):
            pacific.append((0,c))
            atlantic.append((ROWS-1,c))
        
        for r in range(ROWS):
            pacific.append((r,0))
            atlantic.append((r,COLS-1))

        bfs(pacific,pac)
        bfs(atlantic,atl)
        
        
        
        #resultant array we return
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                #if True on both matrix add to the resultant array
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res

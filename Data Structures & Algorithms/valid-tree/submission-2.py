class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        p = {i:[] for i in range(n)}
        visited = set()
        for i,j in edges:
            p[i].append(j)
            p[j].append(i)
        
        #n-1 edges check
        if(len(edges)) != n-1:
            return False
        
        def dfs(x):
            #mark node as visited
            visited.add(x)
            for i in p[x]:
                if i not in visited:
                    dfs(i)
        dfs(0)
        return len(visited) == n
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        #add values to the preMap
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited, cycle = set(), set()
        output = []
        

        def dfs(crs):
            #base case of being visited: loop/cycle
            if crs in cycle:
                return False
            #base case of being empty []
            if crs in visited:
                return True
            
            cycle.add(crs)
            
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

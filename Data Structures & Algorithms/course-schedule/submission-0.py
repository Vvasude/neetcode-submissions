class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}
        for courses, prereq in prerequisites:
            #append i to []
            preMap[courses].append(prereq)
        
        visited = set()
        def dfs(courses):
            #base case of cycle
            if courses in visited:
                return False
            #base case of being empty
            if preMap[courses] == []:
                return True
            visited.add(courses)
            for p in preMap[courses]:
                if not dfs(p):
                    return False
            #remove the course
            visited.remove(courses)
            preMap[courses] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
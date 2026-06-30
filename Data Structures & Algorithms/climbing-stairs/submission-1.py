class Solution:
    def climbStairs(self, n: int) -> int:
        
        #create a cache for O(1) lookup
        
        #rather than repetitive calculations
        memo = {}

        def ways(node):
            
            if node in memo:
                #map[node] because memo is a hashmap
                return memo[node]
            
            #bsase case
            if node == 0:
                return 1
            if node == 1:
                return 1
            
            res = ways(node-1) + ways(node-2)
            #add res to memo
            memo[node] = res
            #return memo
            return res
        
        return ways(n)

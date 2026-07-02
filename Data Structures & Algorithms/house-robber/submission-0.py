class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        #base case
        n = len(nums)
        if n == 0:
            return 0

        def ways(node):
            if node in memo:
                return memo[node]
            if node < 0:
                return 0
            if node == 0:
                return nums[0]
            memo[node] = max(ways(node-1),ways(node-2)+nums[node])
            return memo[node]
        
        return ways(n-1)
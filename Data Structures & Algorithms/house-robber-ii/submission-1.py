class Solution:
    def rob(self, nums: List[int]) -> int:
    
        return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1]))
    
    
    def helper(self, nums):
        #setup 2 houses and initialize their costs as 0
        rob1,rob2 = 0,0
        for num in nums:
            #num will translate to choose this house
            robHouse = max(rob1+num,rob2)
            rob1 = rob2
            rob2 = robHouse

        return rob2
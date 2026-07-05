class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMax,curMin, best = nums[0],nums[0],nums[0]

        for i in range(1, len(nums)):
            temp = curMax
            curMax = max(curMax*nums[i], curMin*nums[i], nums[i])
            curMin = min(temp*nums[i], curMin*nums[i], nums[i])

            best = max(best,curMax)
        return best
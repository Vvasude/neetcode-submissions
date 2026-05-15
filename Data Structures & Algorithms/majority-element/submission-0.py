class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        n = len(nums)

        for i in range(len(nums)):
            seen[nums[i]] = 1+seen.get(nums[i],0)
        for key,count in seen.items():
            if count > n/2:
                return key
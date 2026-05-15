class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()
        L = 0

        for R in range(len(nums)):
            if R-L >k:
                #window is too big so remove and move pointer
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                #found duplicate
                return True
            window.add(nums[R])
        return False
            

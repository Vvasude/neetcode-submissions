class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums)-1
        

        while L<=R:
            mid  = (L+R)//2
            print(mid)
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                R-=1

            elif nums[mid]< target:
                L+=1

        return -1        
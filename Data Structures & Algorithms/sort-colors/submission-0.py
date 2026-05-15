class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # create an occurance array for the 3 values
        count = [0]*3

        # update count to store how many times we have seen that value
        for i in nums:
            count[i] += 1
        #[1,2,1] = 1 zero, 2 ones and 1 two

        token = 0
        for i in range(3):
            while count[i]:
                count[i]-=1
                nums[token] = i
                token+=1
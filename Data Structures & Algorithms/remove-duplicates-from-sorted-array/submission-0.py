class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #create the k pointer to keep track of the unique values
        k = 1
        #we set k =1 because we know the first element will always be unique

        #loop of k+1 values and compare whether they are unique or dupes
        for i in range(1,len(nums)):
            #if they aren't the same swap and add to the counter
            if nums[i]!=nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k
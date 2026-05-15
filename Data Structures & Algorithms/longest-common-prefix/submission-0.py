class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #take first string and compare
        prefix = strs[0]

        #loop through the list and compare with prefix
        for i in range(1,len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                #create a way to break if they dont match anymore
                if prefix[j]!=strs[i][j]:
                    break
                j+=1
            prefix = prefix[:j]
        return prefix

        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #set res as an empty string which also helps with base case of no string
        res = ""
        #resultant length index
        resLen = 0

        for i in range(len(s)):
            #odd length base case
            #create two pointers that we will set to i
            l,r = i,i

            while l>=0 and r<len(s) and s[l]==s[r]:
                #update the pointers
                
                #update the max length
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
            #even length
            l,r = i,i+1    
            while l>=0 and r<len(s) and s[l]==s[r]:
                #update the pointers
                
                #update the max length
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r += 1
        return res
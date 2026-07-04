class Solution:
    def countSubstrings(self, s: str) -> int:
        #create a resultant string to hold the final string
        res = ""
        #create a lengeth checker
        resLen = 0

        for i in range(len(s)):
            #for odd cases
            #set the pointers to the middle
            l,r = i,i
            #while they are a palindrome update our variables
            while l>=0 and r<len(s) and s[l]==s[r]:
                #update res
                res = s[l:r+1]
                #update length
                resLen+=1
                #update pointers
                l-=1
                r+=1
            
            #for even cases
            #set the pointers to the middle
            l,r = i,i+1
            #while they are a palindrome update our variables
            while l>=0 and r<len(s) and s[l]==s[r]:
                #update res
                res = s[l:r+1]
                #update length
                resLen+=1
                #update pointers
                l-=1
                r+=1
        return resLen
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a set because it tells immediately if there is a dupe
        seen = set()
        #create a left pointer
        l = 0
        #create a var to check max substring
        res = 0

        for r in range(len(s)):
            #traverse and remove all counts
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            #otherwise add r and continue count
            seen.add(s[r])
            res = max(res,(r-l)+1)
        return res
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(n):
            if n in memo:
                return memo[n]
            
            if n == len(s):
                return 1
            
            res = 0
            if s[n] != '0':
                res+=dfs(n+1)
            if n+1 < len(s) and 10<= int(s[n:n+2])<=26:
                res+=dfs(n+2)
            
            memo[n] = res
            return res
            

            

        
        return dfs(0)
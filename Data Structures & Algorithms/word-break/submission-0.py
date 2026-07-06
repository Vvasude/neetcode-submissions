class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #create T/F array with index 0 being true
        dp = [True] + [False]*len(s)

        for i in range(1, len(s)+1):
            for word in wordDict:
                start = i-len(word)
                if start >=0 and dp[start] and s[start:i]==word:
                    dp[i] = True
                    break
        return dp[-1]
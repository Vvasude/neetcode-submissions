class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a default dict that will help with key error later on
        res = defaultdict(list)
        for i in range(len(strs)):
            s = ''.join(sorted(strs[i]))
            res[s].append(strs[i])
        return list(res.values())

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        

        for num in nums:
            #creates [freq,number]
            count[num] = 1+count.get(num,0)
        
        #sorting
        arr = []
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()
        
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
            print(res)
        return res
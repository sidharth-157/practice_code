class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        collect = dict()
        for i in range(len(jewels)):
            if jewels[i] not in collect:
                collect[jewels[i]]=0
        count = 0        
        for i in range(len(stones)):
            if stones[i] in collect:
                count+=1
        return count

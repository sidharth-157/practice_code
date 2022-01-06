class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        counter = 0
        length = len(nums)
        
        for i in range(length):
            for j in range(i+1,length):
                if nums[i]==nums[j]:
                    counter+=1
        
        return counter
        

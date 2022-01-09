class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        collect = []
        
        length = len(nums)
        
        for i in range(length):
            #collect[nums[i]]=0
            counter = 0
            for j in range(length):
                if nums[i] > nums[j] and i!=j:
                    #collect[]
                    counter+=1
            collect.append(counter)
            
        return collect
        

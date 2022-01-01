class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        length=len(nums)
        arr=[]
        
        for i in range(length):
            for j in range(i+1,length):
                if target==nums[i]+nums[j]:
                    arr.append(i)
                    arr.append(j)
                    break
        
        return ar


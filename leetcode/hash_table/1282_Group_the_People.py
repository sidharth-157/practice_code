class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        collect = dict()
        length = len(groupSizes)
        
        for i in range(length):
            if groupSizes[i] not in collect:
                collect[groupSizes[i]] = [i]
            else:
                arr=collect[groupSizes[i]]
                arr.append(i)
                collect[groupSizes[i]]=arr
        
        #print(collect)
        
        data = []
        
        for i in collect:
            lenght = len(collect[i])
            j=0
            temp = collect[i]
            while(j<lenght):
                data.append(temp[j:j+i])
                j+=i
        
        #print(data)
        
        return data

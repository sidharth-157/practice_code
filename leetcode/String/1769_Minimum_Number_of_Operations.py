class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        collect = dict()
        collect['1'] = []
        ans = []
        
        length = len(boxes)
        
        for i in range(length):
            if boxes[i]=='1':
                collect['1'].append(i)
                
        for i in range(length):
            agg = 0
            for j in collect['1']:
                agg+=abs(i-j)
            ans.append(agg)
        #print(collect,ans)
        return ans

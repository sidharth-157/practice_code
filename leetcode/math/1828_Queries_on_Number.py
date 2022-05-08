import math
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for query in queries:
            count = 0
            for point in points:
                a = (pow(point[0]-query[0],2))
                b = (pow(point[1]-query[1],2))
                #print(a,b)
                dist = math.sqrt(a+b)
                #print(dist,query[2],query[0],query[1])
                if dist<=query[2]:
                    #print(dist)
                    count+=1
            ans.append(count)
        #rint(ans)
        return ans

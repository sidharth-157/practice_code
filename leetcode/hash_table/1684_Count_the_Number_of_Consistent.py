class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        collect = dict()
        for i in allowed:
            collect[i]=0
        #print(collect)
        
        count=len(words)
        
        for string in words:
            for i in string:
                if i not in collect:
                    count-=1
                    break
        #print(count)
        return count
        

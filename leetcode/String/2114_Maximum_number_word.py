class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        length = len(sentences)
        maxi = 0
        arr = []
        
        
        for i in range(length):
            
            sentence = sentences[i]
            data = sentence.split()
            maxi = len(data)
            arr.append(maxi)
            
        print(arr)
        return(max(arr))

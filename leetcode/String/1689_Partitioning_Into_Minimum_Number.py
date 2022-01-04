class Solution:
    def minPartitions(self, n: str) -> int:
        stack = [0]
        length = len(n)
        for i in range(length):
            data = int(n[i])
            if data > stack[-1]:
                stack.append(data)
                stack.pop(0)
        return stack[-1]
        

class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        i=1
        for ch in s:
            sum+= (ord("z")-ord(ch)+1)*i
            i+=1
        return sum


    
    
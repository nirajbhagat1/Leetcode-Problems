class Solution:
    def largestOddNumber(self, num: str) -> str:

        
        high=0
        lst=list(num)


        for i in range(len(num)-1,-1,-1):
            ch=int(num[i])
            if(ch%2!=0):
                return num[0:i+1]

      
        return ""
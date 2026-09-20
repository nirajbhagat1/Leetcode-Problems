class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        arr=list(range(1,n+1))
        result=[]
        self.printSubArr(arr,[],0,k,result)
        return result
  
        
    
    def printSubArr(self,arr,temp,i,k,result):
        if(len(temp)==k  ):   
            return result.append(temp.copy())
        if(len(arr)==i):
            return
        temp.append(arr[i])
        self.printSubArr(arr,temp,i+1,k,result)
        temp.pop()
        self.printSubArr(arr,temp,i+1,k,result)
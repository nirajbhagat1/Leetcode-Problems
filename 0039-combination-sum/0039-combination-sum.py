class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]

        def findResult(i,temp,target):
            if(target==0):
                result.append(temp.copy())
                return
            if(len(candidates)==i or target<0):
                return
            
            temp.append(candidates[i])
            findResult(i,temp,target-candidates[i])
            temp.pop()
            findResult(i+1,temp,target)
        
        findResult(0,[],target)
        return result


        

    
    
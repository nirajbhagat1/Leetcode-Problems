class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       
       
        i =0
        j=len(nums)-1
       
        while (i<=j):
            if(nums[j]==val):
                j-=1;
                continue;
            
            if(nums[i]==val):
                temp=nums[i];
                nums[i]=nums[j];
                nums[j]=temp
                i+=1;
                j-=1;
            else:
                i+=1;
        return j+1
        
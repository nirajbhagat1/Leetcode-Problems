class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       
        insertPosition =0
       
        for i in range(len(nums)):
            if (nums[i]!=val):
                nums[insertPosition]=nums[i]
                insertPosition+=1

        return insertPosition

        
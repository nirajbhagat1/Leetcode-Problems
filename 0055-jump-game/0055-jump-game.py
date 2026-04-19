# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         max_reach = 0
        
#         for i in range(len(nums)):
#             if i > max_reach:
#                 return False
            
#             max_reach = max(max_reach, i + nums[i])
        
#         return True
# 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True
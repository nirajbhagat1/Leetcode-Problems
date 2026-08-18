# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
#         result=set()
#         current=[]

#         def backtrack(index):
#             if(index==len(nums)):
#                 result.add(tuple(current.copy()))
#                 return
            
#             current.append(nums[index])
#             backtrack(index+1)
#             current.pop()

#             backtrack(index+1)
#         backtrack(0)
#         return list(result)

            
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort to ensure identical subsets have the same element order
        result = set() # Correctly initialize an empty set
        current = []

        def backtrack(index):
            if index == len(nums):
                # Convert the list to a tuple before adding it to the set
                result.add(tuple(current))
                return
            
            # Pick the element
            current.append(nums[index])
            backtrack(index + 1)
            current.pop()

            # Don't pick the element
            backtrack(index + 1)
            
        backtrack(0)
        
        # Convert the tuples back into lists for the final answer
        return [list(subset) for subset in result]
        
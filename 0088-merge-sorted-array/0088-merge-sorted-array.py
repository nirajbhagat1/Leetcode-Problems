# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         lst=[]
#         i=0;
#         j=0;
#         while i<m and j<n :
            
#             if(nums1[i]<nums2[j]){
#                 lst.append(nums1[i] )
#                 i++;
#             }
#              if(nums1[i]>nums2[j]){
#                 lst.append(nums2[j] )
#                 j++;
#             }
#              if(nums1[i]==nums2[j]){
#                  lst.append(nums1[i] )
#                 lst.append(nums2[j] )
#                 j++;
#                 i++;
#             }
#         return lst
        

    
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1   # last element of nums1 (valid part)
        j = n - 1   # last element of nums2
        k = m + n - 1  # last position of nums1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If nums2 still has elements left
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
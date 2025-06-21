class Solution {
    public int search(int[] nums, int target) {
        int n=nums.length;
        int t=target;

        int left=0,right=n-1;

        while(left<=right){
            int mid=(left+right)/2;

            if(nums[mid]==t)return mid;

            
        

            //left sorted
            if(nums[left]<=nums[mid]){
                if(t>=nums[left]&&t<nums[mid]){
                    right=mid-1;
                }
                else{
                    left=mid+1;
                }
            }
            else{
                if(t>nums[mid]&&t<=nums[right]){
                    left=mid+1;
                }
                else{
                    right=mid-1;
                }
            }
        }
        return -1;
    }
}
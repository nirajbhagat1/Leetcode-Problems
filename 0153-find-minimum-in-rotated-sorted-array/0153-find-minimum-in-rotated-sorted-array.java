class Solution {
    public int findMin(int[] nums) {
        int n=nums.length;
        int i=0;
        if(nums[0]>nums[n-1]){
            while(nums[i]>nums[n-1]){
                i++;
            }
        }

        return nums[i];
       
    }
}
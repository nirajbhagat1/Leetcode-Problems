class Solution {
    public int findPeakElement(int[] nums) {
        
        int n=nums.length;
        int max=Integer.MIN_VALUE;
        int maxIndex=0;
        for(int i=0;i<n;i++){
            
            if(nums[i]>max){
                maxIndex=i;
                max=nums[i];
            }
        }
        return maxIndex;

        // if(n<=2){}


        // for(int i=1;i<n-1;i++){
        //     int prev=nums[i-1];
        //     int curr=nums[i];
        //     int next=nums[i+1];
        //     if(curr>prev&& curr>next)return i;
        // }
        // return 0;
    }
}
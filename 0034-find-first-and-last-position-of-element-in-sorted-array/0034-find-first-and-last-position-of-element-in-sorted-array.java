class Solution {
    public int[] searchRange(int[] nums, int target) {
         int left = 0, right = nums.length - 1;

         int[]res={-1,-1};

        while (left <= right) {
            int mid = (left + right) / 2;
            

            if (nums[mid] == target){
                int low=mid,high=mid;
                while(low>=0 && nums[low]==target){
                    res[0]=low;
                    low--;
                }
                 while(high<=nums.length-1 && nums[high]==target){
                    res[1]=high;
                    high++;
                }
                return res;
            }

            // Left part is sorted
            if (nums[left] <= nums[mid]) {
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            // Right part is sorted
            else {
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return res;
        
    }
}
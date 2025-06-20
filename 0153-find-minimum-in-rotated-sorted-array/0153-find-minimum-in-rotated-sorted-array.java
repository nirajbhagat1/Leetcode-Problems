class Solution {
    public int findMin(int[] nums) {
         int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // If mid element is greater than the rightmost, min is to the right
            if (nums[mid] > nums[right]) {
              left=mid+1;
            } else {
                // Min is at mid or to the left
                right=mid;
                ;
            }
        }

        // Left will point to the smallest element
        return nums[left];
    
    }
}
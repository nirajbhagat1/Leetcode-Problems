class Solution {
    public int maxSubArray(int[] arr) {
         int maxSoFar = arr[0];    // \U0001f31f Final answer
        int currentSum = arr[0];  // \U0001f4e6 Current subarray sum

        for (int i = 1; i < arr.length; i++) {
            currentSum = Math.max(arr[i], currentSum + arr[i]); // \U0001f504 Extend or start new?
            maxSoFar = Math.max(maxSoFar, currentSum);          // ✅ Update max
        }

        return maxSoFar;
    }
}
class Solution {
    public int maxProfit(int[] prices) {
        int n= prices.length, min=Integer.MAX_VALUE, max=Integer.MIN_VALUE, max_profit=Integer.MIN_VALUE;
        

        for(int i=0;i<n;i++){
            if (prices[i]<min){
                min=prices[i];
                max=prices[i];
            }
            if(prices[i]>max){
                max=prices[i];
            }
            int profit= max-min;
            max_profit=Math.max(max_profit,profit);
        }
        return max_profit;
    }
}
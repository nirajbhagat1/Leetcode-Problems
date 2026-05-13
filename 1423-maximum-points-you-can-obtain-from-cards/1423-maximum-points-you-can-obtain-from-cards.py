# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:

#         n=len(cardPoints)
        
#         maxPoints=0

#         for i in range(n):
#             if i+1>k:
#                 break
#             maxPoints+=max(cardPoints[i],cardPoints[n-i-1])
#         return maxPoints

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)

        # if taking all cards
        if k == n:
            return sum(cardPoints)

        windowSize = n - k

        totalSum = sum(cardPoints)

        # first window sum
        currSum = sum(cardPoints[:windowSize])

        minSum = currSum

        left = 0

        for right in range(windowSize, n):

            currSum += cardPoints[right]
            currSum -= cardPoints[left]

            left += 1

            minSum = min(minSum, currSum)

        return totalSum - minSum
from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        total=0
       

        substrings = [
            s[i:j]
            for i in range(len(s))
            for j in range(i+1, len(s)+1)
            if len(set(s[i:j])) >= 2
        ]
        for subs in substrings:
            total+=self.countBeauty(subs)
    
        return total

        
    def countBeauty(self,s:str)->int:
        freq=Counter(s)
        values=freq.values()
        return max(values)-min(values)
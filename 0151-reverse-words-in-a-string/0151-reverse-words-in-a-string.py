class Solution:
    def reverseWords(self, s: str) -> str:

        lst=s.strip().split();
        left=0;
        right=len(lst);

        revstr=""
        
        for currstr in reversed(lst):
            if re.fullmatch(r'\s+', currstr):
                continue

            revstr+=currstr.strip()+" "
            
        
        return revstr.strip()

        

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         # Calling .split() without " " handles multiple spaces automatically
#         words = s.split() 
        
#         # Reverse the list of words
#         words.reverse()
        
#         # Join them back together with a single space
#         return " ".join(words)
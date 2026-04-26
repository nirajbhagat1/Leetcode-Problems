

class Solution:
    def reverseWords(self, s: str) -> str:
        # Calling .split() without " " handles multiple spaces automatically
        words = s.split() 
        
        # Reverse the list of words
        words.reverse()
        
        # Join them back together with a single space
        return " ".join(words)
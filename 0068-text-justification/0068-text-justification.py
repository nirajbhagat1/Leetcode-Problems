# class Solution:
#     def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
#         n=len(words)
#         final_lst=[]
#         curr_lst=[]
#         curr_len=0

#         for i in range(n):
#             curr_len+=len(words[i])
             
#              if(curr_len+(i-1))<=maxWidth:
#                  curr_lst.append(words[i])

    

#     def countTotChar((words: List[str])-> int:
#         totLen=0
#         for word in words:
#             totLen+=len(word)
#     return totLen+(len(words)-1)

#     def generateSpaces(lst: List[str],  maxWidth: int) -> List[str]:

#         remaining = maxWidth countTotChar(lst: List[str])
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        line_len = 0

        for word in words:
            # check if adding word exceeds width
            if line_len + len(line) + len(word) > maxWidth:
                res.append(self.justify(line, line_len, maxWidth))
                line = []
                line_len = 0

            line.append(word)
            line_len += len(word)

        # last line (left justified)
        last_line = " ".join(line)
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)

        return res

    def justify(self, line, line_len, maxWidth):
        if len(line) == 1:
            return line[0] + " " * (maxWidth - len(line[0]))

        total_spaces = maxWidth - line_len
        gaps = len(line) - 1

        space = total_spaces // gaps
        extra = total_spaces % gaps

        result = ""

        for i in range(gaps):
            result += line[i]
            result += " " * (space + (1 if i < extra else 0))

        result += line[-1]
        return result
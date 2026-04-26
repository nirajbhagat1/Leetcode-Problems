# class Solution:
#     def removeOuterParentheses(self, s: str) -> str:
#         stack=[]
#         removeStartIndex=[]
#         removeEndIndex=[]

#         for i in range(len(s)):
#             if s[i]=="(":
#                 stack.append('(')
#                 if(len(stack)==1):
#                     removeStartIndex.append(i)
            
#             else:
#                 stack.pop()
#                 if(len(stack)==0):
#                      removeEndIndex.append(i)
    
       
#         lst = list(s)



#         for index in removeStartIndex:
#             lst[index]=""
#         for index in removeEndIndex:
#             lst[index]=""

#         s = "".join(lst)

#         return s
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        depth = 0

        for ch in s:
            if ch == '(':
                if depth > 0:
                    res.append(ch)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res.append(ch)

        return "".join(res)
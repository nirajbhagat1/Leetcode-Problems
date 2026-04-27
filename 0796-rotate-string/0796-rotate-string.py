# class Solution:
#     def rotateString(self, s: str, goal: str) -> bool:

#         if(len(s)!=len(goal)):
#             return False
#         forward1={}
#         forward2={}
#         backward1={}
#         backward2={}

#         for i in range(len(s)):
#             if i==(len(s)-1):
#                 forward1[s[i]]=s[0]
#                 continue
#             forward1[s[i]]=s[i+1]

#         for i in range(len(goal)):
#             if i==(len(goal)-1):
#                 forward2[goal[i]]=goal[0]
#                 continue
#             forward2[goal[i]]=goal[i+1]
        
#         for i in range(len(s)-1,-1,-1):
#             if i==(0):
#                 backward1[s[i]]=s[-1]
#                 continue
#             backward1[s[i]]=s[i-1]

#         for i in range(len(goal)-1,-1,-1):
#             if i==(0):
#                 backward2[goal[i]]=goal[-1]
#                 continue
#             backward2[goal[i]]=goal[i-1]

#         return forward1==forward2 and backward1==backward2


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        return len(s)==len(goal) and goal in (s+s)
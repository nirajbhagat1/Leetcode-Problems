class Solution:
    def maxDepth(self, s: str) -> int:
        md=0
        depth=0
        for ch in s:
            if ch=="(":
                depth+=1
            elif ch==")":
                depth-=1
            md=max(md,depth)
        return md
        
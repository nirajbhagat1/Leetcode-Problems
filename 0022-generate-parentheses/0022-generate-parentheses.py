class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        open=0
        close=0
        result=[]

        def gen(open,close,result,temp,n):
            if(len(temp)==2*n):
                result.append("".join(temp.copy()))
                return
            
            if(open<n):
                temp.append("(")
                gen(open+1,close,result,temp,n)
                temp.pop()
            if(close<open):
                temp.append(")")
                gen(open,close+1,result,temp,n)
                temp.pop()

        gen(open,close,result,[],n)
        return result
        
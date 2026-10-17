class Solution:
    def totalNQueens(self, n: int) -> int:
        def isSafe(i,j):
            # Upper Right Diagonal
            for r,c in zip(range(i,-1,-1), range(j,n)) :
                if(board[r][c]=='Q'):
                    return False
            # Upper Right Diagonal
            for  r,c in zip(range(i,-1,-1), range(j,-1,-1)) :
                if(board[r][c]=='Q'):
                    return False
                                                            
            for r in range(i,-1,-1):
                if(board[r][j]=='Q'):
                    return False
            return True
       

        board=[["." for j in range(n)] for i in range(n)]
        count=0
        def placeQueen(i, j):
            nonlocal count    
            if(i==n):
                count+=1 
                return     
          
            for j in range(n):
                if(isSafe(i,j)):
                    board[i][j]='Q'
                    placeQueen(i+1,j)
                    board[i][j]='.'
                   
        placeQueen(0,0)
        return count


        
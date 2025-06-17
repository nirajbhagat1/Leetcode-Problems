class Solution {
    public void setZeroes(int[][] matrix) {
        int m= matrix.length;
        int n= matrix[0].length;
        int[][] mat=new int[m][n];

         for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                mat[i][j] = matrix[i][j];
            }
        }

        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(matrix[i][j]==0){
                    for(int k=0;k<m;k++){
                        mat[k][j]=0;
                    }
                    for(int l=0;l<n;l++){
                        mat[i][l]=0;
                    }
                }
            }
        }

       for (int i = 0; i < mat.length; i++) {
            for (int j = 0; j < mat[0].length; j++) {
                matrix[i][j] = mat[i][j];
            }
        }

    }
}
// class Solution {
//     public void setZeroes(int[][] matrix) {
//         int m= matrix.length;
//         int n= matrix[0].length;
//         int[][] mat=new int[m][n];

//          for (int i = 0; i < m; i++) {
//             for (int j = 0; j < n; j++) {
//                 mat[i][j] = matrix[i][j];
//             }
//         }

//         for(int i=0;i<m;i++){
//             for(int j=0;j<n;j++){
//                 if(matrix[i][j]==0){
//                     for(int k=0;k<m;k++){
//                         mat[k][j]=0;
//                     }
//                     for(int l=0;l<n;l++){
//                         mat[i][l]=0;
//                     }
//                 }
//             }
//         }

//        for (int i = 0; i < mat.length; i++) {
//             for (int j = 0; j < mat[0].length; j++) {
//                 matrix[i][j] = mat[i][j];
//             }
//         }

//     }
// }
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        boolean firstRowZero = false;
        boolean firstColZero = false;

        // Step 1: Check if first row has zero
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                firstRowZero = true;
                break;
            }
        }

        // Step 2: Check if first column has zero
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
                break;
            }
        }

        // Step 3: Use first row and column as markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;  // Mark row
                    matrix[0][j] = 0;  // Mark column
                }
            }
        }

        // Step 4: Zero out cells based on markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Step 5: Handle first row
        if (firstRowZero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }

        // Step 6: Handle first column
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}

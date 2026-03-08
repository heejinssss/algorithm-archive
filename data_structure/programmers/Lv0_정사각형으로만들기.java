class Solution {
    public int[][] solution(int[][] arr) {
        int[][] answer = {};
        
        int row = arr.length;
        int col = arr[0].length;

        if (row > col) {
            int[][] result = new int[row][row];
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < col; j++) {
                    result[i][j] = arr[i][j];
                }
            }
            return result;
        }

        if (col > row) {
            int[][] result = new int[col][col];
            for (int i = 0; i < col; i++) {
                for (int j = 0; j < row; j++) {
                    result[j][i] = arr[j][i];
                }
            }
            return result;
        }

        return arr;
    }
}

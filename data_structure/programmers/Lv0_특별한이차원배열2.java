class Solution {
    public int solution(int[][] arr) {
        int answer = 0;
        int ci = arr.length;
        int cj = arr.length;

        for (int i = 0; i < ci; i++) {
            for (int j = 0; j < cj; j++) {
                if (arr[i][j] == arr[j][i]) {
                    continue;
                }
                return 0;
            }
        }
        
        return 1;
    }
}

class Solution {
    public int solution(int[][] board, int k) {
        int answer = 0;
        int len_i = board.length;
        int len_j = board[0].length;

        for (int i = 0; i < len_i; i++) {
            for (int j = 0; j < len_j; j++) {
                if (i + j <= k) {
                    answer += board[i][j];
                }
            }
        }

        return answer;
    }
}

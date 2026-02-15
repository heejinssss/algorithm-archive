import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[] query) {

        int[] answer = arr;

        for (int i = 0; i < query.length; i++) {

            int len = answer.length;

            if (i % 2 == 1) { // 홀수 인덱스이면 앞부분 제거
                if (query[i] == len-1) {
                    answer = new int[]{ answer[len-1] };
                } else {
                    answer = Arrays.copyOfRange(answer, query[i], len);
                }
            } else { // 짝수 인덱스이면 뒷부분 제거
                if (query[i] == 0) {
                    answer = new int[]{ answer[0] };
                } else {
                    answer = Arrays.copyOfRange(answer, 0, query[i]+1);
                }                
            }
        }

        return answer;
    }
}

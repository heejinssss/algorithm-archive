import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        ArrayList<Integer> answer = new ArrayList<>();
        int s = 0;
        int e = 0;
        int k = 0;
        
        for (int[] query : queries) {
            s = query[0];
            e = query[1];
            k = query[2];

            // 최대값 구하기
            // int more_than_k = Arrays.stream(arr).max().orElse(0);
            // 적합한 결과값이 없는 경우 -1을 출력하기 위해 최대값+1로 초기 세팅
            int more_than_k = 1000001;

            for (int i = s; i <= e; i++) {
                if (arr[i] > k && more_than_k >= arr[i]) {
                    more_than_k = arr[i];
                }
            }

            if (more_than_k == 1000001) {
                answer.add(-1);
            } else {
                answer.add(more_than_k);
            }

        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}

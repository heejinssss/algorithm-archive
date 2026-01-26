import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int n) {

        for (int idx = arr.length % 2 == 0 ? 1 : 0; idx < arr.length; idx += 2) {
            arr[idx] += n;
        }

        return arr;

        /*
        List<Integer> answer = new ArrayList<>();

        // 1이면 arr의 모든 짝수 인덱스에 n 더하기 (0, 2, 4 ...)
        // 0이면 arr의 모든 홀수 인덱스에 n 더하기 (1, 3, 5 ...)
        int pivot = arr.length % 2;

        for (int idx = 0; idx < arr.length; idx++) {
            if (pivot == 1) {
                answer.add(idx % 2 == 0 ? arr[idx] + n : arr[idx]);
            } else {
                answer.add(idx % 2 == 0 ? arr[idx] : arr[idx] + n);
            };
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
        */
    }
}

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, boolean[] flag) {
        // int[] answer = {};
        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            int count = arr[i];
            if (flag[i]) { // true이면
                while (count > 0) {
                    answer.add(arr[i]);
                    answer.add(arr[i]);
                    count--;
                }
            } else { // false이면
                while (count > 0) {
                    answer.remove(answer.size() - 1);
                    count--;
                }
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}

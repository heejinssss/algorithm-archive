import java.util.*;

class Solution {
    public int[] solution(int[] arr, int k) {

        List<Integer> answer = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            if (!answer.contains(arr[i]) && k > 0) {
                answer.add(arr[i]);
                k--;
            };
        }

        while (k > 0) {
            answer.add(-1);
            k--;
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}

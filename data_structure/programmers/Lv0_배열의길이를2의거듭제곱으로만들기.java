import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        // int[] answer = {};

        /*
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int x : arr) {
            answer.add(x);
        }

        int arr_len = arr.length;
        int count = 1;

        while (true) {
            if (arr_len > count) {
                count *= 2;
            } else {
                for (int i = 0; i < count-arr_len; i++) {
                    answer.add(0);
                }
                break;
            }
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
        */
            
        int count = 1;

        while (count < arr.length) {
            count *= 2;
        }

        return Arrays.copyOf(arr, count);
    }
}

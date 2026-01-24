import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] num_list) {

        return Arrays.stream(num_list).sorted().skip(5).toArray();

        /*
        List<Integer> answer = new ArrayList<>();

        for (int num : num_list) {
            answer.add(num);
        }

        Collections.sort(answer);

        for (int i = 0; i < 5; i++) {
            answer.remove(0);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
        */
    }
}

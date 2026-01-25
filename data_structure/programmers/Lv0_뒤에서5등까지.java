import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int[] num_list) {

        // /* other 1
        return Arrays.stream(num_list)
                     .sorted()
                     .limit(5)
                     .toArray();
        // */

        /* other 2
        Arrays.sort(num_list);

        return Arrays.copyOfRange(num_list, 0, 5);
        */

        /* mine
        List<Integer> answer = new ArrayList<>();
        
        Arrays.sort(num_list);
        
        for (int i = 0; i < 5; i++) {
            answer.add(num_list[i]);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
        */
    }
}

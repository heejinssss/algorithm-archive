import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int idx = num_list.length;
        int[] answer = Arrays.copyOf(num_list, idx + 1);

        if (num_list[idx-1] > num_list[idx-2]) {
            answer[idx] = num_list[idx-1] - num_list[idx-2];
        } else {
            answer[idx] = num_list[idx-1] * 2;
        }
    
        return answer;
    }
}

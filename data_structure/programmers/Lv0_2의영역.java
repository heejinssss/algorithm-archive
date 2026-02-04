import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        List<Integer> twozone = new ArrayList<>();
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                twozone.add(i);
            }
        }

        if (twozone.size() == 0) {
            answer.add(-1);
        } else if (twozone.size() == 1) {
            answer.add(2);
        } else if (twozone.size() > 1) {
            return Arrays.copyOfRange(arr, twozone.get(0), twozone.get(twozone.size()-1)+1);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}

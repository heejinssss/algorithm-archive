import java.util.*;

class Solution {
    public int[] solution(String my_string) {

        char[] chars = my_string.toCharArray();
        List<Integer> list = new ArrayList<>();

        for (char c : chars) {
            if (c >= 48 && c <= 57) {
                list.add(c - 48);
            }
        }

        int[] answer = list.stream().mapToInt(i -> i).toArray();

        Arrays.sort(answer);

        return answer;
    }
}

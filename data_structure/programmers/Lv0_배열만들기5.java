import java.util.ArrayList;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        // int[] answer = {};

        ArrayList<Integer> answer = new ArrayList<>();

        for (String intStr : intStrs) {
            int p = Integer.valueOf(intStr.substring(s, s+l));
            if (k < p) answer.add(p);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}

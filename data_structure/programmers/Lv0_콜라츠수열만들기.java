import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(n);

        while (n != 1) {
            int next = n % 2 == 0 ? n / 2 : n * 3 + 1;
            answer.add(next);
            n = next;
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}

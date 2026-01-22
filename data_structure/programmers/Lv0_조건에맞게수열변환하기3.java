import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int k) {
        ArrayList<Integer> answer = new ArrayList<>();

        for (int i = 0; i < arr.length; i++) {
            answer.add(k % 2 == 0 ? arr[i] + k : arr[i] * k);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}

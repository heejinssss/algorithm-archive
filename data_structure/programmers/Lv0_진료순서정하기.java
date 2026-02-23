import java.util.Arrays;

class Solution {
    public int[] solution(int[] emergency) {

        int[] sorted = Arrays.copyOf(emergency, emergency.length);
        Arrays.sort(sorted);

        int[] answer = new int[emergency.length];

        for (int i = 0; i < emergency.length; i++) {
            answer[i] = emergency.length - Arrays.binarySearch(sorted, emergency[i]);
        }

        return answer;
    }
}

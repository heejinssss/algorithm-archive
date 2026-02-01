import java.util.Arrays;

class Solution {
    public int solution(int[] numbers, int n) {
        int answer = 0;
        int pivot = numbers.length - 1;

        answer = Arrays.stream(numbers).sum();

        for (int i = pivot; i > 0; i--) {
            if (answer - numbers[i] <= n) {
                break;
            } else {
                answer -= numbers[i];
            }
        }

        return answer;
    }
}

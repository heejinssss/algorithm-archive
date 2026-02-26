import java.util.Arrays;

class Solution {
    public int solution(int[] arr) {
        int answer = 0;
		int n = arr.length;

        while (true) {

			int[] pre_arr = Arrays.copyOfRange(arr, 0, n);

			for (int i = 0; i < n; i++) {
                if (arr[i] >= 50 && arr[i] % 2 == 0) {
                    arr[i] = arr[i] / 2;
                } else if (arr[i] < 50 && arr[i] % 2 == 1) {
                    arr[i] = (arr[i] * 2) + 1;
                }
            }

            if (Arrays.equals(arr, pre_arr)) {
                break;
            }

            answer++;
        }

        return answer;
    }
}

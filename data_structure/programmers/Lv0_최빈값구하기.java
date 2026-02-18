// Retry
import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;

        Arrays.sort(array);

        int[] count_arr = new int[array[array.length-1]+1];

        for (int num : array) {
            count_arr[num] += 1;
        }

        Arrays.sort(count_arr);

        int maxCount        = count_arr[count_arr.length-1];
        int maxCountIndex   = count_arr.length-1;

        for (int i = maxCountIndex-1; i > 0; i--) {
            if (maxCount < count_arr[i]) {
                maxCount = count_arr[i];
                maxCountIndex = i;
            } else if (maxCount > count_arr[i]) {
                return i;
            } else if (maxCount == count_arr[i]) {
                return -1;
            }
        }

        return maxCountIndex;
    }
}

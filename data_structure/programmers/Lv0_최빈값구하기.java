import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;

        // 입력 array 오름차순 정렬을 보장하지 않기 때문에 최초 정렬
        Arrays.sort(array);

        int size = array[array.length-1] + 1;
        int[] count_arr = new int[size];

        for (int num : array) {
            count_arr[num] += 1;
        }

        int maxIndex = 0;
        int maxCount = 0;

        for (int i = 0; i < count_arr.length; i++) {
            if (count_arr[i] >= maxCount) {
                maxIndex = i;
                maxCount = count_arr[i];
            }
        }
        
        for (int i = 0; i < count_arr.length; i++) {
            if (count_arr[maxIndex] == count_arr[i] && maxIndex != i) {
                return -1;
            }
        }

        return maxIndex;
    }
}

class Solution {
    public int solution(int[] arr, int idx) {
        // int answer = 0;

        while (idx < arr.length) {
            if (arr[idx] == 1) {
                return idx;
            } else {
                idx++;
            }
        }

        return -1;
        
        /*
        if (idx == arr.length) {
            answer = -1;
        }

        return answer;
        */
    }
}

class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int cur_num = 0;

        for (int num : num_list) {
            answer += Integer.toBinaryString(num).length() - 1;
            // while (num > 0) {
            //     if (num % 2 == 0) {
            //         answer++; num /= 2;
            //     } else {
            //         num -= 1;
            //     }
            // }
        }

        return answer;
    }
}

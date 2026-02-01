class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[num_list.length];

        // 0 ~ n-1
        // n ~ num_list.length

        for (int i = 0, j = 0; i < num_list.length; i++) {
            if (n + i < num_list.length) {
                answer[i] = num_list[n + i];
            } else {
                answer[i] = num_list[j];
                j++;
            }
        }

        return answer;
    }
}

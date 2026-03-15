class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];

        int even = 0;
        int odd  = 0;

        for (int num : num_list) {
            even = num % 2 == 0 ? even+1 : even;
            odd  = num % 2 == 1 ? odd+1  : odd;
        }

        answer[0] = even;
        answer[1] = odd;

        return answer;
    }
}
class Solution {
    public int[] solution(int start_num, int end_num) {

        int pivot = end_num - start_num + 1;
        int[] answer = new int[pivot];

        for (int i = 0; i < pivot; i++) {
            answer[i] = start_num;
            start_num++;
        }

        return answer;
    }
}

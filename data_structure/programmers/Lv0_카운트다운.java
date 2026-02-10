class Solution {
    public int[] solution(int start_num, int end_num) {
        int count = start_num - end_num + 1;
        int[] answer = new int[count];
        
        for (int i = 0; i < count; i++) {
            answer[i] = start_num - i;
        }

        return answer;
    }
}

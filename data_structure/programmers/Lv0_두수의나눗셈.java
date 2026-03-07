class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;

        float result = ((float) num1 / num2) * 1000;

        answer = (int) result;

        return answer;
    }
}

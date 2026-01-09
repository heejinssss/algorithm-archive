class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        String result_by_operator = a + "" + b;
        int result1 = Integer.parseInt(result_by_operator);
        int result2 = 2*a*b;
        
        if (result1 < result2) {
            answer = result2;
        } else {
            answer = result1;
        }

        return answer;
    }
}

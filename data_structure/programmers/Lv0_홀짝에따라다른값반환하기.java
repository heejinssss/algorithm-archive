class Solution {
    public int solution(int n) {
        int answer = 0;
        
        // n이 짝수이면
        if (n % 2 == 0) {
            for (int i = 1; i <= n; i++) {
                if (i % 2 == 0) {
                    answer += (i * i);
                }
            }
        // n이 홀수이면
        } else {
            for (int i = 1; i <= n; i++) {
                if (i % 2 == 1) {
                    answer += i;
                }
            }
        }
        return answer;
    }
}

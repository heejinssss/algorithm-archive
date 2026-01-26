class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        int am = a % 2 == 0 ? 0 : 1;
        int bm = b % 2 == 0 ? 0 : 1;
        int c = Integer.max(a, b);
        int d = Integer.min(a, b);

        answer = (am == 1 && bm == 1) ? a * a + b * b : (am == 0 && bm == 0) ? (c - d) : 2 * (a + b);

        return answer;
    }
}

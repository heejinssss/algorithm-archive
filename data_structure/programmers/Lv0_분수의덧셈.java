class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];

        int numer = (numer1 * denom2) + (numer2 * denom1); // 분자
        int demon = denom1 * denom2; // 분모

        answer[0] = numer / gcd(Integer.max(numer, demon), Integer.min(numer, demon));
        answer[1] = demon / gcd(Integer.max(numer, demon), Integer.min(numer, demon));

        return answer;
    }
    
    private int gcd(int a, int b) {
        int r = a % b; // 나머지
        if (r == 0) {
            return b;
        } else {
            return gcd(b, r); // 작은 수, 나머지
        }
    }
}

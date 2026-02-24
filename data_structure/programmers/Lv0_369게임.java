class Solution {
    public int solution(int order) {
        int answer = 0;

        String order_str = order + "";

        for (int i = 0; i < order_str.length(); i++) {
            char o = order_str.charAt(i);
            if (o == '3' || o == '6' || o == '9') {
                answer++;
            }
        }

        return answer;
    }
}

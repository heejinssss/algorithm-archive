class Solution {
    public String solution(String my_string, int m, int c) {
        String answer = "";

        // m : my_string 길이의 약수
        for (int i = 0; i < my_string.length() / m; i++) {
            answer += my_string.substring(m*i, m*(i+1)).substring(c-1, c);
        }

        return answer;
    }
}

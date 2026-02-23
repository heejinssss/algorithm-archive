class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String num_str = "0";

        for (int i = 0; i < my_string.length(); i++) {
            if (48 <= my_string.charAt(i) && my_string.charAt(i) <= 57) {
                num_str += my_string.substring(i, i+1);
            } else {
                answer += Integer.parseInt(num_str);
                num_str = "0";
            };
        }

        answer += Integer.parseInt(num_str);

        return answer;
    }
}

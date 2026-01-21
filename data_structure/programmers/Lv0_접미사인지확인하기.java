class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;

        if (my_string.endsWith(is_suffix)) {
            answer = 1;
        } else {
            answer = 0;
        }
        
        return answer;

        /*
        int my_string_len = my_string.length();
        int is_suffix_len = is_suffix.length();
        int len = my_string_len - is_suffix_len;

        String pivot = "";

        if (len > -1) {
            pivot = my_string.substring(len);
            if (pivot.equals(is_suffix)) {
                return 1;
            } else {
                return 0;
            }
        } else {
            return 0;
        }
        */
    }
}

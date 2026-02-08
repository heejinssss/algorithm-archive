class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        
        /*
        String[] reverse_strs = new String[e-s+1];

        for (int i = 0; i < e-s+1; i++) {
            reverse_strs[i] = my_string.substring(e-i, e-i+1);
        }
        
        String reverse_str = String.join("", reverse_strs);
        */
        
        StringBuilder reverse_str = new StringBuilder(my_string.substring(s, e+1));

        reverse_str.reverse();

        answer = my_string.substring(0, s) + reverse_str + my_string.substring(e+1);

        return answer;
    }
}

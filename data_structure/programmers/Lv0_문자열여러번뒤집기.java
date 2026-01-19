class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = my_string;
        int s = 0;
        int e = 0;

        for (int[] query: queries) {
            s = query[0];
            e = query[1];

            // 문자열 reverse
            StringBuffer sb = new StringBuffer(answer.substring(s, e+1));
            String reverse_sb = sb.reverse().toString();

            answer  = answer.substring(0, s) +
                      reverse_sb +
                      answer.substring(e+1);
        }
        return answer;
    }
}

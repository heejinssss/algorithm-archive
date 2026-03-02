class Solution {
    public int solution(String s) {
        int answer = 0;

        String[] s_arr = s.split(" ");
        String cur_s = s_arr[0];

        for (String a : s_arr) {
            if (!a.equals("Z")) {
                answer += Integer.parseInt(a);
            } else {
                answer -= Integer.parseInt(cur_s);
            }
            cur_s = a;
        }

        return answer;
    }
}

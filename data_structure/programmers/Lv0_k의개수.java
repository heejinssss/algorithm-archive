class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String str = "";

        for (int s = i; s < j+1; s++) {
            String s_str = s+"";
            String k_str = k+"";
            if (s_str.contains(k_str)) {
                for (int si = 0; si < s_str.length(); si++) {
                    answer = s_str.substring(si, si+1).contains(k_str) ? answer + 1 : answer;
                }
            }
        }

        return answer;
    }
}

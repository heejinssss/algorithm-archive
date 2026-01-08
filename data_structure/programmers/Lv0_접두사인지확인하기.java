class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
    
        if (is_prefix.length() > my_string.length()) {
            return answer;
        }

        String pre = "";
        String str = "";

        for (int i = 0; i < is_prefix.length(); i++) {
            
            pre = is_prefix.substring(i,i+1);
            str = my_string.substring(i,i+1);

            if (!pre.equals(str)) {
                return 0;
            }
        }

        return 1; // 반복문이 정상 종료되는 경우
    }
}

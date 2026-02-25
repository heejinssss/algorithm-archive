class Solution {
    public String solution(String cipher, int code) {
        String answer = "";

        String[] c_arr = cipher.split("");
        
        for (int i = code; i <= c_arr.length; i += code) {
            answer += c_arr[i-1];
        }

        return answer;
    }
}

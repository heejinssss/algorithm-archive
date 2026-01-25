class Solution {
    public int solution(String num_str) {
        int answer = 0;
        
        String[] arr = num_str.split("");

        for (String num : arr) {
            answer += Integer.parseInt(num);
        }

        /*
        for (int i = 0; i < num_str.length(); i++) {
            answer += Integer.parseInt(num_str.substring(i, i+1));
        }
        */

        return answer;
    }
}

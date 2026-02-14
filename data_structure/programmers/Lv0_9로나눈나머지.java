class Solution {
    public int solution(String number) {
        int answer = 0;
        
        for (int i = 0; i < number.length(); i++) {
            int realN = Integer.parseInt(number.substring(i, i + 1));
            answer += realN;
        }

        answer = answer % 9;

        return answer;
    }
}

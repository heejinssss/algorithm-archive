class Solution {
    public int solution(int a, int b) {
        int answer = 0;

        String str1 = "";
        String str2 = "";

        int answer1 = 0;
        int answer2 = 0;

        str1 = String.valueOf(a) + String.valueOf(b);
        str2 = String.valueOf(b) + String.valueOf(a);

        answer1 = Integer.parseInt(str1);
        answer2 = Integer.parseInt(str2);
        
        answer = answer1 > answer2 ? answer1 : answer2;

        return answer;
    }
}

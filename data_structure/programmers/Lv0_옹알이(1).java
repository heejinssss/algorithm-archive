class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        for (String b : babbling) {
            String str1 = b.replaceAll("aya", "x").replaceAll("ye", "x").replaceAll("woo", "x").replaceAll("ma", "x");
            String str2 = str1.replaceAll("x", "");

            if (!str2.equals("")) {
                continue;
            }

            answer++;
        }

        return answer;
    }
}

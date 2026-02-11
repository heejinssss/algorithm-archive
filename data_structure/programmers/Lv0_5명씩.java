class Solution {
    public String[] solution(String[] names) {
        int maxCount = names.length % 5 == 0 ? names.length / 5 : (names.length / 5) + 1;
        String[] answer = new String[maxCount];

        for (int i = 0; i < maxCount; i++) {
            answer[i] = names[i*5];
        }

        return answer;
    }
}

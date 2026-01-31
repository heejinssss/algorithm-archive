import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public String[] solution(String myString) {
        // String[] answer = {};

        // 1. "x" 기준으로 분리
        String[] parts = myString.split("x");

        // 2. 빈 문자열 제거
        List<String> list = new ArrayList<>();
        for (String s : parts) {
            if (!s.equals("")) {
                list.add(s);
            }
        }

        // 3. 배열로 변환
        String[] answer = list.toArray(new String[0]);

        // 4. 사전순 정렬
        Arrays.sort(answer);

        return answer;
    }
}

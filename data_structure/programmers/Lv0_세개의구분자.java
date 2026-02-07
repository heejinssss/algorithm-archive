import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String myStr) {
        List<String> answer = new ArrayList<>();

        String[] parts = myStr.split("[abc]+");

        for (String part : parts) {
            if (!part.equals("")) {
                answer.add(part);
            }
        }

        if (answer.size() == 0) {
            answer.add("EMPTY");
        }

        return answer.toArray(new String[0]);
    }
}

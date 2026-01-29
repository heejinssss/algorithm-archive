import java.util.List;
import java.util.ArrayList;

class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {

        List<String> answer = new ArrayList<>();

        for (int i = 0; i < finished.length; i++) {
            if (!finished[i]) {
                answer.add(todo_list[i]);
            }
        }

        return answer.stream().toArray(String[]::new);
    }
}

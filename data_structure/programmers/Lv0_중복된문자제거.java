import java.util.*;

class Solution {
    public String solution(String my_string) {
        /*
        String answer = "";

        for (int i = 0; i < my_string.length(); i++) {
            if (!answer.contains(my_string.substring(i, i+1))) {
                answer += my_string.substring(i, i+1);
            }
        }

        return answer;
        */

        String[] answer = my_string.split("");

        Set<String> set = new LinkedHashSet<String>(Arrays.asList(answer));

        return String.join("", set);
    }
}
